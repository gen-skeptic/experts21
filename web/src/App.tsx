import { BookOpen, Github, KeyRound, Menu, RotateCcw, X } from "lucide-react";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { ApiError, getCatalog, postJson, stream } from "./api";
import { BrainBadge } from "./components/BrainBadge";
import { Composer } from "./components/Composer";
import { MessageView } from "./components/MessageView";
import { ModelMenu } from "./components/ModelMenu";
import { Sidebar } from "./components/Sidebar";
import { loadConversation, loadModelChoice, saveConversation, saveModelChoice, savePassword } from "./storage";
import type { Assignment, Catalog, ChatMessage, ReplyMeta, TeamMember, TeamRun } from "./types";
import { TEAM_KEY } from "./types";

const REPO_URL = "https://github.com/gen-skeptic/experts21";

type Phase = { kind: "loading" } | { kind: "password"; message: string } | { kind: "error"; message: string } | { kind: "ready" };

const newId = () => (crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`);
const history = (messages: ChatMessage[]) =>
  messages.filter((m) => m.content.trim() && !m.pending && !m.meta?.error).map(({ role, content }) => ({ role, content }));

function PasswordGate({ message, onSubmit }: { message: string; onSubmit: (password: string) => void }) {
  const [value, setValue] = useState("");
  return (
    <main className="center-screen">
      <form
        className="panel gate"
        onSubmit={(e) => {
          e.preventDefault();
          if (value) onSubmit(value);
        }}
      >
        <p className="eyebrow">&gt;_ DIO expert team</p>
        <h1>Password</h1>
        <p>{message}</p>
        <label className="field">
          <span>App password</span>
          <input type="password" value={value} onChange={(e) => setValue(e.target.value)} autoComplete="current-password" autoFocus />
        </label>
        <button type="submit" className="button button-primary" disabled={!value}>
          <KeyRound size={15} aria-hidden /> Continue
        </button>
      </form>
    </main>
  );
}

function autoModelText(catalog: Catalog, taskName: string): string {
  const task = catalog.taskTypes.find((t) => t.name === taskName);
  if (!task) return "the agent's own brain";
  const name = (key: string) => catalog.models.find((m) => m.key === key)?.name ?? key;
  return `${name(task.primary)} for ${task.name.charAt(0).toLowerCase()}${task.name.slice(1)} (${task.tier} tier), fallback ${name(task.fallback)}, then the agent's own Claude brain.`;
}

export function App() {
  const [phase, setPhase] = useState<Phase>({ kind: "loading" });
  const [catalog, setCatalog] = useState<Catalog | null>(null);
  const [selected, setSelected] = useState<string>(TEAM_KEY);
  const [query, setQuery] = useState("");
  const [menuOpen, setMenuOpen] = useState(false);
  const [conversations, setConversations] = useState<Record<string, ChatMessage[]>>({});
  const [busy, setBusy] = useState<Set<string>>(new Set());
  const [modelChoice, setModelChoice] = useState<string>(() => loadModelChoice());
  const controllers = useRef<Record<string, AbortController>>({});
  const endRef = useRef<HTMLDivElement>(null);

  // ------------------------------------------------------------ load the team
  const load = useCallback(async () => {
    setPhase({ kind: "loading" });
    try {
      const c = await getCatalog();
      setCatalog(c);
      setModelChoice((v) => (v === "auto" || v === "claude" || c.models.some((m) => m.key === v) ? v : "auto"));
      if (c.passwordRequired && c.passwordOk !== true) {
        savePassword("");
        setPhase({ kind: "password", message: c.passwordOk === false ? "That password didn't work. Try again." : "The owner of this app set a password, so only people they share it with can spend its API credit." });
      } else setPhase({ kind: "ready" });
    } catch (e) {
      setPhase({ kind: "error", message: e instanceof Error ? e.message : "The app could not load." });
    }
  }, []);
  useEffect(() => {
    void load();
  }, [load]);

  const messages = useMemo(() => conversations[selected] ?? loadConversation(selected), [conversations, selected]);
  useEffect(() => {
    endRef.current?.scrollIntoView({ block: "end" });
  }, [messages]);

  // ------------------------------------------------------------ conversation state helpers
  const setConversation = useCallback((key: string, update: (prev: ChatMessage[]) => ChatMessage[]) => {
    setConversations((all) => {
      const next = update(all[key] ?? loadConversation(key));
      if (!next.some((m) => m.pending)) saveConversation(key, next);
      return { ...all, [key]: next };
    });
  }, []);
  const patchMessage = useCallback(
    (key: string, id: string, patch: (m: ChatMessage) => ChatMessage) => setConversation(key, (prev) => prev.map((m) => (m.id === id ? patch(m) : m))),
    [setConversation],
  );
  const patchTeam = useCallback(
    (id: string, patch: (t: TeamRun) => TeamRun) => patchMessage(TEAM_KEY, id, (m) => ({ ...m, team: patch(m.team ?? { status: "routing", members: [] }) })),
    [patchMessage],
  );
  const setWorking = (key: string, on: boolean) =>
    setBusy((prev) => {
      const next = new Set(prev);
      if (on) next.add(key);
      else next.delete(key);
      return next;
    });

  const handleFailure = (error: unknown): string => {
    if (error instanceof DOMException && error.name === "AbortError") return "Stopped.";
    if (error instanceof ApiError && error.passwordRequired) {
      savePassword("");
      setPhase({ kind: "password", message: "The app password is needed again." });
    }
    return error instanceof Error ? error.message : "Something went wrong.";
  };

  const mergeMeta = (prev: ReplyMeta | undefined, data: Record<string, unknown>): ReplyMeta => ({ ...prev, ...(data as ReplyMeta) });

  // ------------------------------------------------------------ one expert
  async function askAgent(agentId: string, text: string) {
    const choice = modelChoice;
    const user: ChatMessage = { id: newId(), role: "user", content: text };
    const reply: ChatMessage = { id: newId(), role: "assistant", content: "", pending: true, meta: {} };
    const turns = [...history(messages), { role: user.role, content: user.content }];
    setConversation(agentId, (prev) => [...prev, user, reply]);
    const controller = new AbortController();
    controllers.current[agentId] = controller;
    setWorking(agentId, true);
    try {
      await stream(
        "chat",
        { agent: agentId, messages: turns, model: choice },
        (event, data) => {
          if (event === "delta") patchMessage(agentId, reply.id, (m) => ({ ...m, content: m.content + String(data.text ?? "") }));
          else if (event === "thinking") patchMessage(agentId, reply.id, (m) => ({ ...m, meta: { ...m.meta, thinking: true } }));
          else if (event === "meta" || event === "done") patchMessage(agentId, reply.id, (m) => ({ ...m, meta: mergeMeta(m.meta, data) }));
          else if (event === "notice") patchMessage(agentId, reply.id, (m) => ({ ...m, meta: { ...m.meta, notice: String(data.message) } }));
        },
        controller.signal,
      );
    } catch (error) {
      const message = handleFailure(error);
      patchMessage(agentId, reply.id, (m) => ({ ...m, meta: { ...m.meta, error: message } }));
    } finally {
      patchMessage(agentId, reply.id, (m) => ({ ...m, pending: false }));
      setWorking(agentId, false);
      delete controllers.current[agentId];
    }
  }

  // ------------------------------------------------------------ the whole team, routed by the orchestrator
  async function askTeam(text: string) {
    const choice = modelChoice;
    const user: ChatMessage = { id: newId(), role: "user", content: text };
    const reply: ChatMessage = { id: newId(), role: "assistant", content: "", pending: true, team: { status: "routing", members: [] } };
    const turns = [...history(messages), { role: user.role, content: user.content }];
    setConversation(TEAM_KEY, (prev) => [...prev, user, reply]);
    const controller = new AbortController();
    controllers.current[TEAM_KEY] = controller;
    setWorking(TEAM_KEY, true);
    try {
      // 1. The orchestrator decides who answers what, with which task type and model.
      const plan = await postJson<{ summary: string; assignments: Assignment[]; routedBy?: string; notices?: string[] } & ReplyMeta>("team/plan", { messages: turns, model: choice }, controller.signal);
      const members: TeamMember[] = plan.assignments.map((a) => ({ ...a, text: "", status: "waiting", meta: choice === "auto" ? { model: a.modelName } : undefined }));
      const planMeta: ReplyMeta = { model: plan.model, api: plan.api, cost: plan.cost, costEstimated: plan.api === "Claude API" };
      patchTeam(reply.id, (t) => ({ ...t, status: members.length ? "asking" : "combining", summary: plan.summary, members, routedBy: plan.routedBy, planMeta, notices: plan.notices }));

      // 2. Every assigned expert answers its part, all at the same time.
      const answers = await Promise.all(
        members.map(async (member) => {
          const patchMember = (p: Partial<TeamMember> | ((m: TeamMember) => Partial<TeamMember>)) =>
            patchTeam(reply.id, (t) => ({ ...t, members: t.members.map((m) => (m.agent === member.agent ? { ...m, ...(typeof p === "function" ? p(m) : p) } : m)) }));
          let answer = "";
          try {
            patchMember({ status: "streaming" });
            await stream(
              "chat",
              {
                agent: member.agent,
                model: choice,
                taskType: member.taskType,
                ...(choice === "auto" ? { planned: member.model } : {}),
                ...(choice === "claude" ? { brain: member.brain, effort: member.effort } : {}),
                assignment: { original: text, summary: plan.summary, question: member.question, reason: member.reason },
              },
              (event, data) => {
                if (event === "delta") {
                  answer += String(data.text ?? "");
                  patchMember((m) => ({ text: m.text + String(data.text ?? "") }));
                } else if (event === "thinking") patchMember({ thinking: true });
                else if (event === "meta" || event === "done") patchMember((m) => ({ meta: mergeMeta(m.meta, data) }));
                else if (event === "notice") patchMember((m) => ({ meta: { ...m.meta, notice: String(data.message) } }));
              },
              controller.signal,
            );
            patchMember({ status: "done" });
          } catch (error) {
            patchMember({ status: "error", error: handleFailure(error) });
          }
          return { agent: member.agent, text: answer };
        }),
      );
      if (controller.signal.aborted) throw new DOMException("Stopped", "AbortError");

      // 3. The orchestrator combines the answers.
      patchTeam(reply.id, (t) => ({ ...t, status: "combining" }));
      await stream(
        "team/synthesize",
        { messages: turns, summary: plan.summary, answers: answers.filter((a) => a.text.trim()), model: choice },
        (event, data) => {
          if (event === "delta") patchMessage(TEAM_KEY, reply.id, (m) => ({ ...m, content: m.content + String(data.text ?? "") }));
          else if (event === "thinking") patchMessage(TEAM_KEY, reply.id, (m) => ({ ...m, meta: { ...m.meta, thinking: true } }));
          else if (event === "notice") patchMessage(TEAM_KEY, reply.id, (m) => ({ ...m, meta: { ...m.meta, notice: String(data.message) } }));
          else if (event === "meta" || event === "done") patchMessage(TEAM_KEY, reply.id, (m) => ({ ...m, meta: mergeMeta(m.meta, data) }));
        },
        controller.signal,
      );
      patchTeam(reply.id, (t) => ({ ...t, status: "done" }));
    } catch (error) {
      const message = handleFailure(error);
      patchMessage(TEAM_KEY, reply.id, (m) => ({ ...m, meta: { ...m.meta, error: message } }));
      patchTeam(reply.id, (t) => ({ ...t, status: "error" }));
    } finally {
      patchMessage(TEAM_KEY, reply.id, (m) => ({ ...m, pending: false }));
      setWorking(TEAM_KEY, false);
      delete controllers.current[TEAM_KEY];
    }
  }

  // ------------------------------------------------------------ render
  if (phase.kind === "loading") return <main className="center-screen">Loading the team…</main>;
  if (phase.kind === "password")
    return (
      <PasswordGate
        message={phase.message}
        onSubmit={(password) => {
          savePassword(password);
          void load();
        }}
      />
    );
  if (phase.kind === "error" || !catalog)
    return (
      <main className="center-screen">
        <div className="panel gate">
          <p className="eyebrow">&gt;_ DIO expert team</p>
          <h1>Not available</h1>
          <p>{phase.kind === "error" ? phase.message : "The app could not load."}</p>
          <button type="button" className="button button-secondary" onClick={() => void load()}>
            Try again
          </button>
        </div>
      </main>
    );

  const agent = catalog.agents.find((a) => a.id === selected);
  const lead = catalog.agents.find((a) => a.id === catalog.orchestrator);
  const isBusy = busy.has(selected);
  const speaker = agent ? agent.name : `${lead?.name ?? "The orchestrator"} and the team`;

  return (
    <div className={`app${menuOpen ? " menu-open" : ""}`}>
      <header className="topbar">
        <button type="button" className="icon-button menu-toggle" onClick={() => setMenuOpen((o) => !o)} aria-label="Toggle the list of experts">
          {menuOpen ? <X size={18} /> : <Menu size={18} />}
        </button>
        <img className="brand-logo" src="/mark.svg" alt="Dautel Intelligent Operations" width="24" height="24" />
        <p className="brand">
          DIO expert team <span className="brand-sub">Experts21 · AI consulting and deployment, Boynton Beach, Florida</span>
        </p>
        <p className="top-links">
          <a href={`${REPO_URL}/blob/main/docs/how-to-talk-to-your-experts.md`} target="_blank" rel="noopener noreferrer" title="How to talk to the experts">
            <BookOpen size={16} aria-hidden /> <span>Guide</span>
          </a>
          <a href={REPO_URL} target="_blank" rel="noopener noreferrer" title="Source on GitHub">
            <Github size={16} aria-hidden /> <span>GitHub</span>
          </a>
        </p>
      </header>
      <aside className="side">
        <Sidebar
          catalog={catalog}
          selected={selected}
          busy={busy}
          query={query}
          onQuery={setQuery}
          onSelect={(key) => {
            setSelected(key);
            setMenuOpen(false);
          }}
        />
        <p className="source">
          {catalog.agents.length} agents from {catalog.source}, built {new Date(catalog.generated).toLocaleDateString()}. AI agents named after Star Trek characters; not people.
        </p>
      </aside>
      <main className="chat">
        {!catalog.configured ? (
          <p className="banner">
            This site may not have model access yet. The owner adds <code>ANTHROPIC_API_KEY</code> or <code>OPENROUTER_API_KEY</code> in Netlify (Project configuration → Environment variables) and redeploys. Questions may fail until then.
          </p>
        ) : !catalog.providers.openrouter && modelChoice !== "claude" ? (
          <p className="banner">
            OpenRouter isn't set up on this site (<code>OPENROUTER_API_KEY</code>), so Auto uses only the Claude models in the catalog.
          </p>
        ) : null}
        <section className="chat-head">
          {agent ? (
            <>
              <div className="chat-title">
                <h1>
                  {agent.name} <span>{agent.title}</span>
                </h1>
                <BrainBadge alias={agent.brain} brains={catalog.brains} effort={agent.effort} />
              </div>
              <p className="job">{agent.job}</p>
              <dl className="persona">
                <div>
                  <dt>Named after</dt>
                  <dd>
                    {agent.fullName}, <em>{agent.series}</em>
                  </dd>
                </div>
                <div>
                  <dt>Voice</dt>
                  <dd>{agent.voice}</dd>
                </div>
                <div>
                  <dt>Working style</dt>
                  <dd>{agent.style}</dd>
                </div>
                <div>
                  <dt>Brain</dt>
                  <dd>
                    {catalog.brains[agent.brain]?.family} (<code>{agent.brain}</code>), effort {agent.effort}. {agent.why}
                  </dd>
                </div>
                <div>
                  <dt>Model on Auto</dt>
                  <dd>{autoModelText(catalog, agent.taskType)}</dd>
                </div>
                <div>
                  <dt>Knowledge</dt>
                  <dd>
                    <code>knowledge/{agent.id}/</code>: {agent.knowledgeFiles.length} {agent.knowledgeFiles.length === 1 ? "document" : "documents"}, plus {agent.docs.length} research{" "}
                    {agent.docs.length === 1 ? "file" : "files"} and {agent.skills.length} {agent.skills.length === 1 ? "skill" : "skills"}
                  </dd>
                </div>
              </dl>
            </>
          ) : (
            <>
              <div className="chat-title">
                <h1>
                  Ask the whole team <span>routed by {lead ? `${lead.name}, ${lead.title}` : "the orchestrator"}</span>
                </h1>
              </div>
              <p className="team-intro">
                {lead?.name ?? "The orchestrator"} reads your question, picks the experts and the model each one needs, asks them in parallel, and combines their answers into one, with
                risks, next steps and the decisions that stay with Erich.
              </p>
            </>
          )}
          {messages.length ? (
            <button type="button" className="button button-ghost clear" disabled={isBusy} onClick={() => setConversation(selected, () => [])} title="Clear this conversation">
              <RotateCcw size={14} aria-hidden /> New conversation
            </button>
          ) : null}
        </section>
        <section className="messages" aria-live="polite">
          {messages.length === 0 ? (
            <p className="empty">
              {agent
                ? `Ask ${agent.name} a question: ${agent.job.charAt(0).toLowerCase()}${agent.job.slice(1)}`
                : "Ask a question that needs more than one expert, for example: Should we take a $9,000 intake-agent build for a 12-attorney law firm next month?"}
            </p>
          ) : (
            messages.map((m) => <MessageView key={m.id} message={m} catalog={catalog} speaker={speaker} />)
          )}
          <div ref={endRef} />
        </section>
        <Composer
          busy={isBusy}
          placeholder={agent ? `Message ${agent.name}…` : "Ask the whole team…"}
          tools={
            <ModelMenu
              catalog={catalog}
              value={modelChoice}
              disabled={isBusy}
              onChange={(v) => {
                setModelChoice(v);
                saveModelChoice(v);
              }}
            />
          }
          onSend={(text) => void (agent ? askAgent(agent.id, text) : askTeam(text))}
          onStop={() => controllers.current[selected]?.abort()}
        />
      </main>
    </div>
  );
}

import { AlertTriangle, Loader2 } from "lucide-react";
import type { Catalog, ChatMessage, ReplyMeta, TeamMember } from "../types";
import { BrainBadge } from "./BrainBadge";
import { Markdown } from "./Markdown";
import { money } from "./ModelMenu";

export function metaLine(m: ReplyMeta | undefined): string | null {
  if (!m || !m.model) return null;
  const via = m.api === "OpenRouter" && m.provider ? `OpenRouter (${m.provider})` : m.api;
  const cost = typeof m.cost === "number" ? `${money(m.cost)}${m.costEstimated ? " est." : ""}` : null;
  return [m.model, via, m.taskType, m.effort ? `effort ${m.effort}` : null, cost].filter(Boolean).join(" · ");
}

function Meta({ message }: { message: ChatMessage }) {
  const line = metaLine(message.meta);
  return line ? <p className="reply-meta">{line}</p> : null;
}

function Member({ member, catalog }: { member: TeamMember; catalog: Catalog }) {
  const working = member.status === "waiting" || member.status === "streaming";
  return (
    <details className={`member member-${member.status}`} open={member.status !== "waiting"}>
      <summary>
        <span className="member-name">
          <strong>{member.name}</strong> <small>{member.title}</small>
        </span>
        {member.meta?.model ? <span className="model-tag">{member.meta.model}</span> : <BrainBadge alias={member.brain} brains={catalog.brains} effort={member.effort} />}
        {working ? <Loader2 className="spin" size={14} aria-label="Working" /> : null}
      </summary>
      <p className="member-question">
        <em>Asked:</em> {member.question || "the original question"}
        {member.reason ? <span className="member-reason"> — {member.reason}</span> : null}
        {member.taskType ? <span className="member-reason"> ({member.taskType})</span> : null}
      </p>
      {member.meta?.notice ? <p className="notice-line member-question">{member.meta.notice}</p> : null}
      {member.error ? (
        <p className="error-line">
          <AlertTriangle size={14} aria-hidden /> {member.error}
        </p>
      ) : member.text ? (
        <Markdown text={member.text} />
      ) : member.thinking ? (
        <p className="thinking-line">Thinking…</p>
      ) : null}
      {member.status === "done" && metaLine(member.meta) ? <p className="reply-meta">{metaLine(member.meta)}</p> : null}
    </details>
  );
}

export function MessageView({ message, catalog, speaker }: { message: ChatMessage; catalog: Catalog; speaker: string }) {
  if (message.role === "user") {
    return (
      <article className="message message-user">
        <p className="who">You</p>
        <div className="bubble">{message.content}</div>
      </article>
    );
  }
  const team = message.team;
  return (
    <article className="message message-assistant" aria-busy={message.pending}>
      <p className="who">{speaker}</p>
      {team ? (
        <div className="team-run">
          <p className="team-status">
            {team.status === "routing" ? "Routing your question…" : null}
            {team.status === "asking" ? `Asking ${team.members.length} ${team.members.length === 1 ? "expert" : "experts"} in parallel…` : null}
            {team.status === "combining" ? "Combining the answers…" : null}
            {team.status === "done" && team.members.length ? `Answered with ${team.members.map((m) => m.name).join(", ")}.` : null}
          </p>
          {team.summary ? <p className="team-summary">{team.summary}</p> : null}
          {team.planMeta?.model ? <p className="reply-meta">Routing plan: {metaLine(team.planMeta)}</p> : null}
          {(team.notices ?? []).map((n) => (
            <p key={n} className="notice-line">
              {n}
            </p>
          ))}
          {team.members.map((m) => (
            <Member key={m.agent} member={m} catalog={catalog} />
          ))}
        </div>
      ) : null}
      {message.content ? (
        <div className="bubble bubble-assistant">
          <Markdown text={message.content} />
        </div>
      ) : message.pending && (!team || team.status === "combining") ? (
        <div className="bubble bubble-assistant">
          <Loader2 className="spin" size={16} aria-hidden /> <span className="thinking-line">{message.meta?.thinking ? "Thinking…" : "Working…"}</span>
        </div>
      ) : null}
      {message.meta?.notice ? <p className="notice-line">{message.meta.notice}</p> : null}
      {message.meta?.error ? (
        <p className="error-line">
          <AlertTriangle size={14} aria-hidden /> {message.meta.error}
        </p>
      ) : null}
      <Meta message={message} />
    </article>
  );
}

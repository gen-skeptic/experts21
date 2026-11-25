import { AlertTriangle, Loader2 } from "lucide-react";
import type { Catalog, ChatMessage, TeamMember } from "../types";
import { BrainBadge } from "./BrainBadge";
import { Markdown } from "./Markdown";

function Meta({ message }: { message: ChatMessage }) {
  const m = message.meta;
  if (!m || !m.model) return null;
  return <p className="reply-meta">{[m.model, m.effort ? `effort ${m.effort}` : null].filter(Boolean).join(" · ")}</p>;
}

function Member({ member, catalog }: { member: TeamMember; catalog: Catalog }) {
  const working = member.status === "waiting" || member.status === "streaming";
  return (
    <details className={`member member-${member.status}`} open={member.status !== "waiting"}>
      <summary>
        <span className="member-name">
          <strong>{member.name}</strong> <small>{member.title}</small>
        </span>
        <BrainBadge alias={member.brain} brains={catalog.brains} effort={member.effort} />
        {working ? <Loader2 className="spin" size={14} aria-label="Working" /> : null}
      </summary>
      <p className="member-question">
        <em>Asked:</em> {member.question || "the original question"}
        {member.reason ? <span className="member-reason"> — {member.reason}</span> : null}
      </p>
      {member.error ? (
        <p className="error-line">
          <AlertTriangle size={14} aria-hidden /> {member.error}
        </p>
      ) : member.text ? (
        <Markdown text={member.text} />
      ) : member.thinking ? (
        <p className="thinking-line">Thinking…</p>
      ) : null}
      {member.model ? <p className="reply-meta">{member.model}</p> : null}
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

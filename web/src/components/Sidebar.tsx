import { Search, Users } from "lucide-react";
import type { Catalog } from "../types";
import { TEAM_KEY } from "../types";
import { BrainBadge } from "./BrainBadge";

interface Props {
  catalog: Catalog;
  selected: string;
  busy: Set<string>;
  query: string;
  onQuery: (q: string) => void;
  onSelect: (key: string) => void;
}

export function Sidebar({ catalog, selected, busy, query, onQuery, onSelect }: Props) {
  const q = query.trim().toLowerCase();
  const visible = catalog.agents.filter(
    (a) => !q || [a.name, a.fullName, a.title, a.id, a.group, a.job].some((s) => s.toLowerCase().includes(q)),
  );
  const lead = catalog.agents.find((a) => a.id === catalog.orchestrator);
  return (
    <nav className="sidebar" aria-label="Experts">
      <button
        type="button"
        className={`team-button${selected === TEAM_KEY ? " is-active" : ""}`}
        onClick={() => onSelect(TEAM_KEY)}
        aria-current={selected === TEAM_KEY ? "page" : undefined}
      >
        <Users size={18} strokeWidth={1.6} aria-hidden />
        <span>
          <strong>Ask the whole team</strong>
          <small>{lead ? `${lead.name} routes your question to the right experts` : "Routed by the orchestrator"}</small>
        </span>
        {busy.has(TEAM_KEY) ? <span className="dot" aria-label="Working" /> : null}
      </button>
      <label className="search">
        <Search size={15} strokeWidth={1.6} aria-hidden />
        <input
          type="search"
          value={query}
          onChange={(e) => onQuery(e.target.value)}
          placeholder={`Search ${catalog.agents.length} experts`}
          aria-label="Search experts"
        />
      </label>
      <div className="agent-groups">
        {catalog.groups.map((group) => {
          const agents = visible.filter((a) => a.group === group);
          if (agents.length === 0) return null;
          return (
            <section key={group}>
              <h2>{group}</h2>
              <ul>
                {agents.map((a) => (
                  <li key={a.id}>
                    <button
                      type="button"
                      className={`agent-row${selected === a.id ? " is-active" : ""}`}
                      onClick={() => onSelect(a.id)}
                      aria-current={selected === a.id ? "page" : undefined}
                      title={`${a.voice} ${a.style}`}
                    >
                      <span className="agent-row-main">
                        <strong>{a.name}</strong>
                        <small>{a.title}</small>
                      </span>
                      <BrainBadge alias={a.brain} brains={catalog.brains} />
                      {busy.has(a.id) ? <span className="dot" aria-label="Working" /> : null}
                    </button>
                  </li>
                ))}
              </ul>
            </section>
          );
        })}
        {visible.length === 0 ? <p className="empty">No expert matches “{query}”.</p> : null}
      </div>
    </nav>
  );
}

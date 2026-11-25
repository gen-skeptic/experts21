// Types for agents-data.generated.js, which scripts/build-agents.mjs writes at build time.
export interface KnowledgeDoc {
  file: string;
  text: string;
}

export interface AgentRecord {
  id: string;
  name: string;
  fullName: string;
  series: string;
  title: string;
  group: string;
  job: string;
  voice: string;
  style: string;
  brain: string;
  effort: string;
  why: string;
  skills: string[];
  docs: string[];
  knowledge: KnowledgeDoc[];
  knowledgeSkipped: string[];
  prompt: string;
}

export interface BrainRecord {
  label: string;
  family: string;
  strengths: string;
  cost: string;
}

export interface AgentsData {
  generated: string;
  source: string;
  orchestrator: string;
  groups: string[];
  /** Agent ids in roster order. */
  order: string[];
  brains: Record<string, BrainRecord>;
  agents: Record<string, AgentRecord>;
  skills: Record<string, string>;
  docs: Record<string, string>;
}

export declare const DATA: AgentsData;

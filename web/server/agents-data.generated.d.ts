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

export interface ModelRecord {
  name: string;
  maker: string;
  /** OpenRouter model ID. */
  openrouter: string;
  /** Claude API model ID, for Claude models. */
  anthropic: string | null;
  /** USD per million tokens. */
  input: number;
  output: number;
  cache_read: number;
  context: number;
  gpqa: number;
  gpqa_cost: number;
  gpqa_s: number;
  tau: number;
  tau_cost: number;
  tau_s: number;
  /** Reasoning efforts the model accepts. */
  efforts: string[];
  note: string;
  /** Average cost of one GPQA plus one tau2 benchmark task, USD. */
  task_cost: number;
}

export interface TaskTypeRecord {
  name: string;
  tier: string;
  primary: string;
  fallback: string;
  effort: string;
  why: string;
  examples: string;
  claude_brain: string;
}

export interface ModelCatalog {
  date: string;
  sources: { label: string; url: string }[];
  tiers: Record<string, { label: string; gpqa: number; tau: number; why: string }>;
  models: Record<string, ModelRecord>;
  task_types: TaskTypeRecord[];
  roles: { routing: { primary: string; fallback: string; effort: string; why: string }; synthesis: { task_type: string } };
  agent_task_type: Record<string, string>;
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
  catalog: ModelCatalog;
}

export declare const DATA: AgentsData;

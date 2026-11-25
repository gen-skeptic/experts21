export type BrainAlias = "haiku" | "sonnet" | "opus" | "fable";
export type Effort = "low" | "medium" | "high" | "xhigh" | "max";

export interface Agent {
  id: string;
  name: string;
  fullName: string;
  series: string;
  title: string;
  group: string;
  job: string;
  voice: string;
  style: string;
  brain: BrainAlias;
  effort: Effort;
  why: string;
  skills: string[];
  docs: string[];
  knowledgeFiles: string[];
  taskType: string;
}

export interface ModelInfo {
  key: string;
  name: string;
  maker: string;
  input: number;
  output: number;
  gpqa: number;
  tau: number;
  taskCost: number;
  claude: boolean;
  note: string;
}

export interface TaskTypeInfo {
  name: string;
  tier: string;
  primary: string;
  fallback: string;
  effort: string;
}

/** "auto", "claude" or a model key from the catalog. */
export type ModelChoice = string;

export interface Brain {
  label: string;
  family: string;
  strengths: string;
  cost: string;
}

export interface Catalog {
  agents: Agent[];
  groups: string[];
  brains: Record<string, Brain>;
  orchestrator: string;
  configured: boolean;
  providers: { claude: boolean; claudeKey: boolean; openrouter: boolean; zdr: boolean };
  models: ModelInfo[];
  taskTypes: TaskTypeInfo[];
  catalogDate: string;
  passwordRequired: boolean;
  passwordOk?: boolean;
  source: string;
  generated: string;
}

export interface ReplyMeta {
  /** Display name of the model, for example "Claude Sonnet 5.5". */
  model?: string;
  modelId?: string;
  api?: string;
  provider?: string | null;
  taskType?: string;
  cost?: number | null;
  costEstimated?: boolean;
  brain?: string;
  effort?: string;
  notice?: string;
  error?: string;
  thinking?: boolean;
}

export interface Assignment {
  agent: string;
  name: string;
  title: string;
  question: string;
  taskType: string;
  model: string;
  modelName: string;
  brain: BrainAlias;
  effort: Effort;
  reason: string;
}

export interface TeamMember extends Assignment {
  text: string;
  status: "waiting" | "streaming" | "done" | "error";
  thinking?: boolean;
  error?: string;
  meta?: ReplyMeta;
}

export interface TeamRun {
  status: "routing" | "asking" | "combining" | "done" | "error";
  summary?: string;
  members: TeamMember[];
  routedBy?: string;
  /** Which model made the routing plan, and what it cost. */
  planMeta?: ReplyMeta;
  notices?: string[];
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  pending?: boolean;
  meta?: ReplyMeta;
  team?: TeamRun;
}

export const TEAM_KEY = "__team__";

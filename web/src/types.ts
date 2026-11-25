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
}

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
  passwordRequired: boolean;
  passwordOk?: boolean;
  source: string;
  generated: string;
}

export interface ReplyMeta {
  model?: string;
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
  brain: BrainAlias;
  effort: Effort;
  reason: string;
}

export interface TeamMember extends Assignment {
  text: string;
  status: "waiting" | "streaming" | "done" | "error";
  thinking?: boolean;
  error?: string;
  model?: string;
}

export interface TeamRun {
  status: "routing" | "asking" | "combining" | "done" | "error";
  summary?: string;
  members: TeamMember[];
  routedBy?: string;
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

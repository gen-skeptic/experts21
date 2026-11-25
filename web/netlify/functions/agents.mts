// GET /api/agents: the sidebar. Names, roles, personalities and brains only; prompts and knowledge stay on the server.
import type { Config } from "@netlify/functions";
import { DATA } from "../../server/agents-data.generated.js";
import { env } from "../../server/env.js";
import { json, passwordOk, passwordRequired } from "../../server/http.js";

export default async (req: Request) => {
  const agents = DATA.order
    .map((id) => DATA.agents[id])
    .map((a) => ({
      id: a.id,
      name: a.name,
      fullName: a.fullName,
      series: a.series,
      title: a.title,
      group: a.group,
      job: a.job,
      voice: a.voice,
      style: a.style,
      brain: a.brain,
      effort: a.effort,
      why: a.why,
      skills: a.skills,
      docs: a.docs,
      knowledgeFiles: a.knowledge.map((d) => d.file),
    }));
  return json(200, {
    agents,
    groups: DATA.groups,
    brains: DATA.brains,
    orchestrator: DATA.orchestrator,
    configured: env("ANTHROPIC_API_KEY") !== "",
    passwordRequired: passwordRequired(),
    passwordOk: req.headers.has("x-app-password") ? passwordOk(req) : undefined,
    source: DATA.source,
    generated: DATA.generated,
  });
};

export const config: Config = { path: "/api/agents", method: "GET" };

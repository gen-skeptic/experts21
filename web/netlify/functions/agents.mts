// GET /api/agents: the sidebar and the model menu. Names, roles, personalities, brains and the model catalog only;
// prompts and knowledge stay on the server.
import type { Config } from "@netlify/functions";
import { DATA } from "../../server/agents-data.generated.js";
import { aiConfigured, claudeSource } from "../../server/claude.js";
import { gatewayAllowed } from "../../server/gateway.js";
import { json, passwordOk, passwordRequired } from "../../server/http.js";
import { openrouterReady, openrouterSource, zdrEnforced } from "../../server/openrouter.js";
import { CATALOG } from "../../server/route.js";

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
      taskType: CATALOG.agent_task_type[a.id],
    }));
  const models = Object.entries(CATALOG.models).map(([key, m]) => ({
    key,
    name: m.name,
    maker: m.maker,
    input: m.input,
    output: m.output,
    gpqa: m.gpqa,
    tau: m.tau,
    taskCost: m.task_cost,
    claude: !!m.anthropic,
    note: m.note,
  }));
  const taskTypes = CATALOG.task_types.map((t) => ({ name: t.name, tier: CATALOG.tiers[t.tier]?.label ?? t.tier, primary: t.primary, fallback: t.fallback, effort: t.effort }));
  return json(200, {
    agents,
    groups: DATA.groups,
    brains: DATA.brains,
    orchestrator: DATA.orchestrator,
    configured: aiConfigured() || openrouterReady(),
    // Which keys the functions see (never their values): "own", "netlify-gateway" (Netlify's injected key, unused
    // unless ALLOW_NETLIFY_AI_GATEWAY=true) or "none".
    providers: {
      claude: aiConfigured(),
      openrouter: openrouterReady(),
      claudeSource: claudeSource(),
      openrouterSource: openrouterSource(),
      gatewayAllowed: gatewayAllowed(),
      zdr: zdrEnforced(),
    },
    models,
    taskTypes,
    catalogDate: CATALOG.date,
    passwordRequired: passwordRequired(),
    passwordOk: req.headers.has("x-app-password") ? passwordOk(req) : undefined,
    source: DATA.source,
    generated: DATA.generated,
  });
};

export const config: Config = { path: "/api/agents", method: "GET" };

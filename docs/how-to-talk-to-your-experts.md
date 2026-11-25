# How to talk to your experts

The team lives in this repository: 50 expert agents in `.claude/agents/` and the skills they share in `.claude/skills/`. Each one has a Star Trek name and personality: Picard (`orchestrator`) runs the team, Cogley (`business-attorney`) reads every clause, Seven (`lean-six-sigma-lead`) won't automate waste, Odo (`quality-reviewer`) lets nothing past; the full list is in [agent-brains.md](agent-brains.md). Open the repository in Claude Code (claude.ai/code, or the `claude` command in a terminal on the laptop) and talk to them in three ways.

## 1. Ask one expert

Type `@agent-` followed by the expert's name, then the question. Claude Code autocompletes the names as you type.

```text
@agent-business-attorney A 12-attorney firm wants us to accept unlimited liability for anything the intake agent says. What do we push back with, and what's our fallback clause?
```

```text
@agent-lean-six-sigma-lead A community association manager says owner requests take five days to answer. How would you run the health check, and what would make you say "fix first"?
```

```text
@agent-cpa-bookkeeper If we sell a research report to many clients, is it subject to Florida sales tax? What about a one-client assessment report?
```

```text
@agent-seo-specialist Give me ten local search terms a law firm administrator in Palm Beach County would type when looking for AI help, ranked by buying intent.
```

```text
@agent-market-research-analyst Which three segments within 10 miles of Boynton Beach should we approach first, and why? Use docs/local-prospects.md.
```

Use one expert when the question clearly belongs to one role. The full list, with each expert's one-line job, is in [expert-roster.md](expert-roster.md).

## 2. Ask the whole team

Start with `@agent-orchestrator`. The orchestrator restates the question, picks the experts it needs (usually two to five), has them work **in parallel**, and returns **one** answer: the recommendation, what each expert said, where they disagree, risks, next steps with owners, and the decisions only Erich can make.

```text
@agent-orchestrator <your question>. Bring in the experts and give me one answer.
```

### Four team prompts that make several experts work together

**1. Take the job or not**

```text
@agent-orchestrator A 12-attorney personal-injury firm in Boynton Beach wants a governed intake agent built next month for $9,000. Should we take it? Check the fit and the employer boundary, the scope and price against our rate card, the security and legal terms, whether we have the hours, and what could go wrong. Give me one recommendation with conditions.
```

Likely experts: `business-development`, `ai-solutions-engineer`, `operations-finance-manager` (price and hours), `security-compliance`, `business-attorney`, `delivery-lead`.

**2. Launch a campaign to one segment**

```text
@agent-orchestrator Plan our Q1 2027 launch to community association managers within 10 miles of Boynton Beach: the offer and price, the fix-first story, the first workshop, the LinkedIn and email plan, what we must not claim, and how we'll measure it. Run the experts in parallel and combine their answers into one plan with owners and dates.
```

Likely experts: `market-research-analyst`, `product-manager`, `lean-six-sigma-lead`, `marketing-director`, `content-marketing`, `business-attorney`, `marketing-analyst`.

**3. Go full-time or not**

```text
@agent-orchestrator Using the numbers in docs/, tell me what has to be true for me to go full-time in 2028, how far we are from the trigger, the tax and insurance changes, and the strongest argument against doing it. I want options, a recommendation and a review date.
```

Likely experts: `operations-finance-manager`, `cpa-bookkeeper`, `insurance-risk-advisor`, `advisory-board`, `talent-people-partner`.

**4. A risky build, done safely**

```text
@agent-orchestrator A three-dentist practice wants an AI front-desk agent that answers patient texts and books appointments. What would it take to do this safely and legally (HIPAA, BAA, Florida texting rules), how would we design and test it, and what should we charge? Have the experts review each other's parts before you combine them.
```

Likely experts: `security-compliance`, `business-attorney`, `senior-agent-engineer`, `cto-principal-architect`, `qa-test-automation-engineer`, `operations-finance-manager`, then `quality-reviewer`.

### If the orchestrator returns a routing plan

Some runtimes, including some cloud sessions, don't let a subagent call other subagents (the setting is `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`). Then the orchestrator returns a **ROUTING PLAN FOR THE MAIN SESSION**, and Claude Code (following `CLAUDE.md`) runs those experts in parallel itself and hands their answers back to the orchestrator to combine. You get the same single answer; it just takes one extra hop. On the laptop, the default lets the orchestrator call the experts directly.

## 3. Run a method directly

Every skill can also be run as a slash command, without naming an expert:

```text
/contract-review Review the attached MSA against our standard positions.
```

```text
/red-team-review Our plan is to raise assessment prices to $5,000 in January.
```

```text
/break-even-and-cash-flow Model 2027 with three assessments a quarter and two retainers by June.
```

```text
/model-selection We need 40 LinkedIn post variants and a client-final SOW this week. Which model for each, through which API, and roughly what will it cost?
```

## 4. In the browser

The web app (<https://dio-experts21.netlify.app>) has the same experts. Pick one in the sidebar, or **Ask the whole team**. The **Model** menu under the message box chooses who answers: **Auto** (the most cost-efficient model for the kind of work, from [model-catalog.md](model-catalog.md)), **Claude** (each expert's own brain, as here) or one model of your choice. The line under each answer shows the model and what it cost.

## Tips for good answers

- **Pull first.** If you added a document on GitHub, start with "First pull the latest from main."
- **Point to the source.** Name the `docs/` file or knowledge document you want used, and ask the expert to **list the documents it used**.
- **Say what decision it's for** and any limit ("at most three experts", "under 300 words", "options and a recommendation").
- **Ask for a review** when it will leave the team: "have `quality-reviewer` check it".
- **Money, ethics and final deployments stay with you.** The experts recommend; you decide.
- **If an answer is off,** say what you expected and ask `@agent-agent-builder` to fix that agent or skill.

## On the laptop (Omarchy / Arch Linux)

Install Claude Code with the official installer, clone the repository and start it from the repository folder:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
git clone https://github.com/gen-skeptic/experts21.git ~/experts21
```

```bash
cd ~/experts21 && claude
```

Then type the prompts above. Run `git pull` first whenever documents were added on GitHub.

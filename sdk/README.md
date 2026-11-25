# Ask an expert from code (Claude Agent SDK)

`ask-cogley.mjs` asks **Cogley** (`business-attorney`) a question from the command line with the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview), so other programs can use the expert too. It loads the agent from `../.claude/agents/business-attorney.md` (instructions, model, effort and skills), adds its knowledge folder `../knowledge/business-attorney/`, runs it as the main agent with read-only tools (`Read`, `Grep`, `Glob`, `WebSearch`, `WebFetch`) in this repository, and prints the answer.

## Run it on the laptop (Omarchy / Arch Linux)

You need Node.js 18 or newer and an Anthropic API key (create one at platform.claude.com → API keys).

1. Install Node.js if it isn't there yet (`node --version` to check):

   ```bash
   sudo pacman -S --needed nodejs npm
   ```

   Omarchy also ships `mise`; `mise use --global node@22` works as well.

2. Install the SDK:

   ```bash
   cd ~/experts21/sdk
   ```

   ```bash
   npm install
   ```

3. Check that Cogley loads. This calls no model and costs nothing:

   ```bash
   npm run check
   ```

4. Set your API key for this terminal. `read -rs` keeps it out of your shell history:

   ```bash
   read -rs ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY
   ```

   (or `export ANTHROPIC_API_KEY="your-key"`)

5. Ask a question:

   ```bash
   node ask-cogley.mjs "Should we sign the Example Law Group MSA as written?"
   ```

The tools Cogley uses are listed as it works, and the answer ends with the documents it used. **Each real question is billed to your API key** (the cost is printed at the end; a contract question on Cogley's Opus brain cost about $0.11 in testing). `npm run check` never is.

## Ask a different expert

Change `AGENT` at the top of `ask-cogley.mjs`, or set it for one run:

```bash
EXPERT_AGENT=lean-six-sigma-lead node ask-cogley.mjs "How would you run a process health check for a property manager?"
```

Any name in `../.claude/agents/` works.

## How it works

| Step | What happens |
| --- | --- |
| Load | Parses the agent file's frontmatter (`name`, `description`, `tools`, `model`, `effort`, `skills`) and body, and reads every text document in its knowledge folder (README first, `archive/` skipped, 150,000-character budget) |
| Define | Passes the agent to `query()` as a programmatic agent (`options.agents`) whose prompt is the agent's instructions plus its knowledge documents, and runs it as the main thread (`options.agent`) |
| Limit | `allowedTools` holds only the read-only tools; `disallowedTools` removes `Write`, `Edit`, `Bash` and `Agent`; `permissionMode: "dontAsk"` denies anything else instead of asking |
| Context | `cwd` is the repository root and `settingSources: ["project"]` loads the project skills, so the agent's skills and `docs/` are there too |
| Answer | Streams the run, prints each tool call to stderr, then the final answer and its cost |

Tested November 25, 2026 with `@anthropic-ai/claude-agent-sdk` 0.3.322 on Node.js 22: `npm run check` passed, and a question about the sample MSA in Cogley's knowledge folder returned an in-character answer with the top three things to negotiate and the documents used.

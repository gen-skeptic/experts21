# Exports

Agents packaged as standalone Claude skills, so you can consult them from any Claude chat without this repository.

| Skill | Agent | What it does |
| --- | --- | --- |
| [`cogley-business-attorney.zip`](cogley-business-attorney.zip) ([contents](cogley-business-attorney/)) | Cogley (`business-attorney`) | Reviews contracts, MSAs, SOWs, NDAs, DPAs, BAAs and client redlines against the firm's standard positions, and Florida business compliance, for review by a licensed attorney |

Each skill folder holds `SKILL.md` (the agent's personality, instructions and how to use its methods), `methods/` (its skills), `knowledge/` (its knowledge folder) and `research/` (the `docs/` files it relies on).

**Everything in the zip goes into your Claude account, including the knowledge files.** Check them for anything private before you upload. The one in Cogley's folder today is a fictional sample MSA.

## Upload it to Claude

1. Download the zip: on GitHub open `exports/cogley-business-attorney.zip` and click the download button, or in a terminal on the laptop:

   ```bash
   curl -LO https://github.com/gen-skeptic/experts21/raw/main/exports/cogley-business-attorney.zip
   ```

2. In Claude, open **Customize → Skills → Add → Upload skill** and choose the zip.
3. In any chat, ask "Ask Cogley whether this MSA is fair" and attach the contract.

## Rebuild it

After changing the agent, its skills, its knowledge folder or the research, rebuild and check the zip (it unzips into an empty folder and checks the frontmatter, the size and every file `SKILL.md` points to):

```bash
python3 tools/export_skill.py business-attorney --verify
```

Any other agent works the same way, for example `python3 tools/export_skill.py lean-six-sigma-lead --verify`.

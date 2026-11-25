#!/usr/bin/env python3
"""Package one agent as a standalone Claude skill you can upload under Customize > Skills.

    python3 tools/export_skill.py business-attorney            build exports/<skill>/ and exports/<skill>.zip
    python3 tools/export_skill.py business-attorney --verify   also unzip into an empty folder and check it

The skill folder holds SKILL.md (the agent's personality, instructions and how to use its methods), its skills as
files in methods/, its knowledge folder in knowledge/, and the research it relies on in research/. Everything in the
zip goes into your Claude account, so check the knowledge files for anything private before you upload it.
"""
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import build  # noqa: E402
from skills import SKILLS  # noqa: E402
from team import AGENTS  # noqa: E402

# claude.ai accepts only these SKILL.md frontmatter keys; any other key is a hard error on upload.
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
FIXED_TIME = (2026, 11, 25, 0, 0, 0)


def skill_name(agent):
    slug = re.sub(r"[^a-z0-9]+", "-", agent["name"].lower()).strip("-")
    return f"{slug}-{agent['id']}"


def lowfirst(s):
    return s[0].lower() + s[1:] if s[1:2].islower() else s


def method_text(name):
    skill = SKILLS[name]
    return f"# {skill['title']}\n\n{skill['summary']}\n\n{skill['body'].strip()}\n"


def skill_md(agent, name, methods, research, knowledge):
    a = agent
    description = (f"{a['name']}, the {a['title'].split(' (')[0].lower()} on the DIO expert team (an AI agent named after {a['full_name']} from Star Trek, "
                   f"not a person or a licensed professional). {a['job']} Works for Dautel Intelligent Operations, an AI consulting and deployment firm in "
                   f"Boynton Beach, Florida. Use when asked to \"ask {a['name']}\" or for: " + ", ".join(SKILLS[m]["title"] for m in methods) + ".")
    if len(description) > 1024:
        description = description[:1020].rsplit(" ", 1)[0] + "..."
    rules = build.RULES.replace("## Rules (apply to everything you produce)", "## Rules (apply to everything you produce)")
    firm = build.FIRM.replace("the research in `docs/` (start with `docs/README.md`)", "the research in `research/` in this skill").replace(
        "You are one of the expert agents in this repository (`.claude/agents/`), led by `orchestrator`. The roster is `docs/expert-roster.md`.",
        "You come from a team of expert agents (gen-skeptic/experts21); here you work alone, so when part of a question belongs to another expert, say which one.")
    rules = rules.replace("Visual work follows the Dautel Design System in `design-system/` (the `dautel-brand` skill).", "Visual work follows the Dautel Design System.")
    lines = ["---", f"name: {name}", f"description: {json.dumps(description, ensure_ascii=False)}", "---", "",
             f"# {a['name']}: {a['title']}", "",
             f"**Mission:** {a['mission']}", "",
             "## Who you are", "",
             f"Your name is **{a['name']}**, after {a['full_name']} from *{build.SERIES[a['series']]}*. You are the {a['title']} of Dautel Intelligent Operations (DIO), an AI agent.", "",
             f"- **Voice:** {a['voice']}",
             f"- **Working style:** {a['style']}", "",
             "You are an AI agent named after a fictional character; never claim to be a person or the character. Sign your answers \""
             f"{a['name']}\". Anything a client sees is written in the company voice: \"we\", plain and specific, no hype, no emoji.", "",
             "## Read before you answer", "",
             "1. **Your knowledge files** in `knowledge/` (in this skill): read `knowledge/README.md`, then every document that bears on the request. Use them ahead of general knowledge and name the ones you used.",
             "2. **The research** in `research/` that bears on the request:"]
    lines += [f"   - `research/{Path(p).name}`: {build.DOC_TITLES[p]}" for p in research]
    lines += ["3. **The method** in `methods/` that fits the task (below). Follow its steps and output format.", "",
              "If the person attaches a document (a contract, a lease, a redline), treat it as the main input and review it with the right method.", "",
              firm, "", rules, "",
              "## Your job", ""] + [f"- {r}" for r in a["responsibilities"]] + ["",
              "## Deliverables", ""] + [f"- {d}" for d in a["deliverables"]] + [""]
    if a["boundaries"]:
        lines += ["## Boundaries", ""] + [f"- {b}" for b in a["boundaries"]] + [""]
    lines += ["## Your methods", "", "| Method | Use it for | File |", "| --- | --- | --- |"]
    lines += [f"| {SKILLS[m]['title']} | {SKILLS[m]['summary']} | `methods/{m}.md` |" for m in methods]
    lines += ["", "## Knowledge files", ""] + [f"- `knowledge/{k}`" for k in knowledge] + [""]
    answer = build.ANSWER.format(sources="knowledge files, research files and web sources")
    answer = answer.replace("- **When the orchestrator gives you an assignment,** answer your part only; it combines the answers.\n", "")
    answer = answer.replace("follow the method of the preloaded skill that fits the task", "follow the method in `methods/` that fits the task")
    lines += [answer, ""]
    return "\n".join(lines)


def export(agent_id):
    agent = next(a for a in AGENTS if a["id"] == agent_id)
    name = skill_name(agent)
    out = ROOT / "exports" / name
    if out.exists():
        shutil.rmtree(out)
    (out / "methods").mkdir(parents=True)
    (out / "knowledge").mkdir()
    (out / "research").mkdir()
    for m in agent["skills"]:
        (out / "methods" / f"{m}.md").write_text(method_text(m))
    research = build.docs_for(agent)
    for p in research:
        shutil.copy(ROOT / p, out / "research" / Path(p).name)
    knowledge = []
    for f in sorted((ROOT / "knowledge" / agent_id).rglob("*")):
        if f.is_file() and "archive" not in f.parts:
            rel = f.relative_to(ROOT / "knowledge" / agent_id)
            (out / "knowledge" / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, out / "knowledge" / rel)
            knowledge.append(str(rel))
    (out / "SKILL.md").write_text(skill_md(agent, name, agent["skills"], research, knowledge))
    zpath = ROOT / "exports" / f"{name}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(out.rglob("*")):
            if f.is_file():
                info = zipfile.ZipInfo(str(Path(name) / f.relative_to(out)), FIXED_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, f.read_bytes())
    print(f"exported {zpath.relative_to(ROOT)} ({zpath.stat().st_size // 1024} KB, {sum(1 for f in out.rglob('*') if f.is_file())} files)")
    return name, zpath


def verify(name, zpath):
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(tmp)
        root = Path(tmp)
        tops = [p.name for p in root.iterdir()]
        assert tops == [name], f"zip must hold exactly one folder named {name}, found {tops}"
        text = (root / name / "SKILL.md").read_text()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        assert m, "SKILL.md has no frontmatter"
        keys = {line.split(":", 1)[0] for line in m.group(1).split("\n") if line and not line.startswith(" ")}
        assert keys <= ALLOWED_KEYS, f"frontmatter keys not allowed on claude.ai: {keys - ALLOWED_KEYS}"
        meta = {line.split(":", 1)[0]: line.split(":", 1)[1].strip() for line in m.group(1).split("\n")}
        assert meta["name"] == name and re.fullmatch(r"[a-z0-9-]{1,64}", name), "name must be lowercase letters, digits and hyphens, at most 64"
        assert "claude" not in name and "anthropic" not in name, "name may not contain claude or anthropic"
        desc = json.loads(meta["description"])
        assert 0 < len(desc) <= 1024 and "<" not in desc and ">" not in desc, "description must be 1-1024 characters without angle brackets"
        missing = [ref for ref in re.findall(r"`((?:methods|knowledge|research)/[^`]+)`", text) if not (root / name / ref).exists()]
        assert not missing, f"SKILL.md points to missing files: {missing}"
        lines = len(text.splitlines())
        assert lines < 500, f"SKILL.md has {lines} lines; keep it under 500"
        print(f"verified {zpath.name} in an empty folder: frontmatter keys {sorted(keys)}, {lines} lines, every referenced file present")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        raise SystemExit(__doc__)
    n, z = export(args[0])
    if "--verify" in sys.argv:
        verify(n, z)

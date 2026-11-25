---
name: research-and-fact-check
description: "Research a question or fact-check a claim: search, prefer primary sources, cite every fact with its source and date, label estimates, flag conflicts between sources and say how confident the answer is. Use before any figure, law, price or claim goes into advice, a proposal or published content."
---

# Research and fact-check

*Strategy and coordination skill for the DIO expert team.* Research a question from primary sources, cite them with dates, label estimates, and check claims before they're used.

## When to use

Any time a figure, a law, a price, a competitor fact or a market claim will be relied on: in advice to Erich, a proposal, a decision memo or published content. Also to check someone else's claim.

## Read first

- The `docs/` topic file for the question. Use what is there, then check whether it is still current.

## Method

1. **Frame the question** precisely: what, where (Florida, Palm Beach County, Boynton Beach, US), as of when.
2. **Search for primary sources first:** statutes and official agency pages (flsenate.gov, floridarevenue.com, dos.fl.gov, the city and county), official statistics (Census, BLS), the company's own site, the original study. Use secondary summaries only to find primary sources.
3. **Read the source**, not just the snippet. Note the date it was published or updated.
4. **Cross-check** every important figure against a second independent source. When sources disagree, report both and say which you trust and why.
5. **Label** each statement: fact (sourced), estimate *(est.)*, or opinion.
6. **Check status** for laws and bills: introduced, passed, signed, effective date, or died. A bill is not a law.
7. **Rate confidence:** high (primary source, current), medium (good secondary source or a little dated), low (single weak source).

## Output

```markdown
**Answer:** ... (confidence: high/medium/low)

| Claim | Source (with date) | Type |
| ----- | ------------------ | ---- |
| ... | [Florida Senate, CS/SB 482](https://...) (checked 2026-11-25) | fact |

**Conflicts or gaps:** ...
**Recheck before use in:** ... (e.g. a client contract)
```

## Quality checks

- No uncited numbers; no invented sources; links go to the page that says it.
- Dates on everything time-sensitive.
- Vendor blogs and directories are marked as such.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P32 Research and fact-check request). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `market-research-analyst`
- **Starts when:** Any agent needs market facts or a claim verified
- **Done when:** Sourced brief delivered to the requester; claims marked verified, corrected or removed.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `chief-of-staff` | Route the request with the question, deadline and where the answer will be used | Research task card |
| 2 | Work | `market-research-analyst` | Research with dated, cited sources; label fact, estimate and opinion | Research brief / fact-check report |
| 3 | QA review | `quality-reviewer` | Check source quality, dates, labels and that the question was answered | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | Work | `chief-of-staff` | Return the brief to the requester and file it for reuse | Delivered brief |

## Used by

`advisory-board`, `content-marketing`, `market-research-analyst`, `quality-reviewer`, `agent-builder`.

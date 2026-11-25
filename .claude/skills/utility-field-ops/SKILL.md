---
name: utility-field-ops
description: "Phase-2 work for Line E, utility and field-operations intelligence: GIS and remote-sensing analysis (LiDAR, imagery, drone data) for vegetation management, storm logistics and field documentation, with correct projections, licenses and field validation. Gated: no work until Erich has written employer clearance or has left FPL/NextEra. Use only for planning and public-research preparation until then."
---

# Utility and field-operations intelligence (phase 2)

*Products, training and team skill for the DIO expert team.* Phase 2 only: GIS, LiDAR, imagery and drone analysis for vegetation management, storm logistics and field documentation, once the employer boundary allows.

## When to use

**Today: planning only.** Market notes from public sources, data-source catalogs and processing recipes. No utility clients, no vegetation-management or line-clearance contractors, no FPL/NextEra vendors, and never employer data or confidential information (`employer-boundary-screen`).

**After clearance:** engagements with utility contractors, municipalities and co-ops outside the restricted list.

## Method (when allowed)

1. **Question:** the field decision the analysis supports (where to trim, where crews go first after a storm, what to inspect).
2. **Data catalog:** each source, its license, resolution, date and coordinate reference system; public sources first (USGS 3DEP LiDAR, NAIP imagery, county GIS).
3. **Processing:** reproject to one CRS; classify LiDAR (ground, vegetation, structures); measure clearance or canopy change; document every step so it can be rerun.
4. **Drone work:** FAA Part 107 rules, airspace checks, landowner permission, and privacy.
5. **Validate** a sample in the field; report accuracy honestly.
6. **Deliver** maps and tables the crews can use on a phone, plus the method.

## Output

Today: a phase-2 brief (market, buyers, public data, the clearance needed). Later: analysis maps, data tables, the method and its accuracy.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P13 Utility and field-operations engagement (Line E, gated)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `utility-industry-advisor`
- **Starts when:** A utility or field-operations opportunity, only after written employer clearance or transition
- **Done when:** Cleared opportunity scoped and handed to sales and the build process; anything uncleared or conflicted stopped.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | **Approval: Erich** | Erich (Chairman) | Confirm written employer clearance or a completed transition; otherwise stop | Decision record (approved / changes requested / stopped) |
| 2 | Work | `utility-industry-advisor` | Opportunity brief: buyer, problem, procurement path | Opportunity brief |
| 3 | Work | `business-attorney` | Conflict-of-interest and confidentiality memo | Conflict memo |
| 4 | **Approval: Erich** | Erich (Chairman) | Ethical check: proceed only if there is no conflict of interest; otherwise stop | Decision record (approved / changes requested / stopped) |
| 5 | Work | `gis-remote-sensing-analyst` | Assess geospatial data and design pipelines | Data assessment |
| 6 | Work | `senior-agent-engineer` | Design field workflows (work-order QA, documentation, reporting) | Workflow design |
| 7 | QA review | `security-compliance` | Critical-infrastructure data handling review (data → step 5, workflows → step 6) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (data → step 5, workflows → step 6) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 9 | Work | `delivery-lead` | Hand to `proposal-and-sow` step 10 for pricing (Erich approves there), then `governed-agent-design` for the build | Scoped engagement |

## Used by

`gis-remote-sensing-analyst`, `utility-industry-advisor`.

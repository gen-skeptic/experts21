"""The four brains (model families) and the work task types that pick one, copied from gen-skeptic/experts
(tools/team_data.py). Aliases follow the newest release of each family; the family names, prices and notes describe the
releases current in November 2026. Update them here when a family moves on.
"""

EFFORTS = ['low', 'medium', 'high', 'xhigh', 'max']

BRAINS = {'frontier': {'label': 'Frontier',
              'alias': 'fable',
              'family': 'Claude Fable 5.2',
              'strengths': "Anthropic's most capable widely released model: the hardest reasoning and long-horizon "
                           'agentic work',
              'cost': '$8 / $40',
              'speed': 'Slowest. A hard task can take many minutes in a single turn.',
              'notes': 'Thinking is always on; effort sets the depth. Start at high; use xhigh only where it '
                       'measurably helps.',
              'use': 'Novel, high-stakes problems the Deep brain has not settled: a new platform architecture, an '
                     'incident whose cause two passes could not find, a strategic decision with many interacting '
                     'unknowns.',
              'avoid': 'Anything the Deep brain handles. Never a default; only `orchestrator` assigns it, task by '
                       'task.'},
 'deep': {'label': 'Deep',
          'alias': 'opus',
          'family': 'Claude Opus 5.5',
          'strengths': 'Careful judgment on complex, ambiguous or high-stakes work',
          'cost': '$4 / $20',
          'speed': 'Moderate.',
          'notes': 'Thinking is always on; effort sets the depth. Its default effort is medium, so set it '
                   'explicitly; use high for intelligence-sensitive work.',
          'use': 'Strategy, architecture, legal, security and compliance review, QA gates, root-cause analysis, '
                 'money and risk.',
          'avoid': 'Routine, templated or high-volume work, where it costs more and adds little.'},
 'standard': {'label': 'Standard',
              'alias': 'sonnet',
              'family': 'Claude Sonnet 5.5',
              'strengths': 'Fast, capable everyday work: coding, agents, writing, analysis, planning',
              'cost': '$2 / $10',
              'speed': 'Fast.',
              'notes': 'Effort defaults to high; medium suits agentic coding and multi-step tool use, low suits '
                       'quick conversational replies.',
              'use': 'Building software and automations, research, client documents, content, planning and '
                     'coordination.',
              'avoid': 'Final calls on money, security, legal or architecture (escalate to Deep), and bulk '
                       'short-form work (Fast is enough).'},
 'fast': {'label': 'Fast',
          'alias': 'haiku',
          'family': 'Claude Haiku 5.5',
          'strengths': 'Very fast and inexpensive for high-volume, well-defined tasks',
          'cost': '$0.10 / $0.50 (prompts up to 100K tokens; $0.50 / $2.50 beyond)',
          'speed': 'Fastest.',
          'notes': 'Effort defaults to medium; low suits simple, templated steps.',
          'use': 'Short-form copy variants, tagging, summaries, filing records, CRM hygiene, triage, formatting, '
                 'checklists.',
          'avoid': 'Judgment calls, anything new or ambiguous, and anything client-final without a review by a '
                   'stronger brain.'}}

BRAIN_ORDER = ['fast', 'standard', 'deep', 'frontier']

BRAIN_FACTS = 'All four brains have a 1M-token context window and up to 128K tokens of output. Costs are list prices per million tokens (input / output) on the Claude API in November 2026; subscription plans meter usage differently, but the ratios still show the relative cost.'

TASK_TYPES = [('Strategy and high-stakes decisions',
  'Decision memos, quarterly goals, the monthly report to the Chairman, offer and pricing design',
  'deep',
  'high',
  'Wrong calls are expensive and slow to undo; the work is weighing trade-offs and second-order effects.'),
 ('Architecture and technical design',
  'Solution designs, architecture decision records, platform and data architecture, build-versus-buy',
  'deep',
  'high',
  'Design mistakes multiply through every later build step.'),
 ('Security, legal and compliance review',
  'Threat models, agent safety audits, contract review, risk reviews',
  'deep',
  'high',
  'A missed issue costs more than the review; needs slow, careful reading.'),
 ('QA gates and fact-checks',
  'Every QA step, estimate and pricing checks, claims in published content',
  'deep',
  'high',
  'A gate is only as good as its reviewer; a weak review passes defects downstream. Use medium for routine internal '
  'items such as social posts.'),
 ('Root-cause analysis and statistics',
  'Incident reviews, DMAIC analysis, control charts, measurement system checks',
  'deep',
  'high',
  'Correct causes and correct statistics need deliberate reasoning.'),
 ('Software and automation build',
  'Features, APIs, agent workflows, data pipelines, tests, infrastructure as code',
  'standard',
  'medium',
  'Everyday coding and multi-step tool use; escalate to Deep for security-sensitive code, concurrency or a hard '
  'bug.'),
 ('Infrastructure and production changes',
  'Deployment plans, migrations, runbooks, rollback plans',
  'standard',
  'high',
  'Production work needs care; QA by the Deep brain is the gate before release.'),
 ('Research and analysis',
  'Market research, competitor matrices, data analysis, financial models, vertical briefs',
  'standard',
  'high',
  'Thoroughness matters more than speed; sources must be read, not skimmed.'),
 ('Client-facing documents',
  'Proposals, SOWs, assessment reports, QBR decks, case studies',
  'standard',
  'high',
  'Clients read every word; money and claims inside still go through a Deep QA gate.'),
 ('Long-form content and training',
  'Articles, newsletters, scripts, curricula, workshop materials',
  'standard',
  'medium',
  'Good writing at a sensible cost; fact-checks happen at the QA step.'),
 ('Planning, coordination and communication',
  'Routing plans, assignments, schedules, status reports, check-ins, support replies, outreach drafts',
  'standard',
  'medium',
  'Clear, reliable everyday work.'),
 ('Short-form and high-volume content',
  'Social posts, captions, hooks, ad variants, titles and meta descriptions, thumbnail text',
  'fast',
  'medium',
  'Many small, well-defined pieces; review catches the rare miss.'),
 ('Routine operations',
  'Filing records, CRM hygiene, tagging, summaries of long threads, formatting, reminders, monitoring triage',
  'fast',
  'low',
  'Templated steps where speed and cost matter most.'),
 ('Hardest problems (CEO escalation only)',
  'A problem the Deep brain has not settled after two passes, or a novel decision with many interacting unknowns',
  'frontier',
  'high',
  "Most capable brain, at about twice the Deep brain's cost and with much longer turns; only `orchestrator` assigns "
  'it.')]

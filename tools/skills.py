"""Every project skill, by category. The bodies live in the skills_*.py files; build.py writes .claude/skills/<name>/SKILL.md."""

from skills_business import BUSINESS, PRODUCTS
from skills_delivery import DELIVERY, PROCESS, SOFTWARE
from skills_marketing import MARKETING
from skills_strategy import SALES, STRATEGY

CATEGORIES = [
    "Strategy and coordination",
    "Sales and clients",
    "Process improvement",
    "AI and platform delivery",
    "Software delivery",
    "Legal, finance and people",
    "Marketing",
    "Products, training and team",
]

SKILLS = {}
for group in (STRATEGY, SALES, PROCESS, DELIVERY, SOFTWARE, BUSINESS, MARKETING, PRODUCTS):
    for name, skill in group.items():
        if name in SKILLS:
            raise ValueError(f"duplicate skill {name}")
        SKILLS[name] = skill

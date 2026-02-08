# LLM Output Auditor

Automated quality auditing framework for LLM outputs using a failure taxonomy + severity grading, combining rule-based validation with LLM-as-a-judge scoring, and root-cause analysis of systematic failures.

## Why this project
LLM applications need more than “average score” evaluation. This project treats evaluation as an **audit** problem:
- classify failures (type + severity)
- standardize auditing criteria
- identify patterns that drive failures (root-cause analysis)

## What it does
1. Generates LLM responses for a benchmark prompt set (`data/prompts.jsonl`)
2. Audits outputs with:
   - rule-based checks (JSON validity, bullet constraints, word limits)
   - LLM-as-a-judge scoring and structured rationale
3. Produces:
   - per-item audit records (`results/audits.jsonl`)
   - root-cause metrics (failure rate vs constraint complexity)
   - a human-readable report (`results/summary_report.md`)

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
# add OPENAI_API_KEY

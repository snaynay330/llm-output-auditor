# LLM Output Auditor

An automated quality auditing and root-cause analysis framework for Large Language Model (LLM) outputs, designed to identify, classify, and diagnose systematic failure modes in instruction-following tasks.

## Why this project
Most LLM evaluation focuses on aggregate scores. In practice, production systems require **auditable quality signals**:
- What failed?
- How severe was the failure?
- Why did it happen?
- Which prompt characteristics increase risk?

This project treats LLM evaluation as a **quality auditing problem**, not just benchmarking.

## What this system does
1. Generates LLM responses for a structured benchmark of prompts
2. Audits each response using:
   - Rule-based validation (format, length, constraint checks)
   - LLM-as-a-judge scoring with structured rationale
3. Classifies failures using a defined taxonomy and severity scale
4. Performs root-cause analysis to correlate failures with prompt complexity
5. Produces a human-readable audit report

## Failure taxonomy
- instruction_violation
- non_answer_or_partial
- hallucination_or_unsupported
- verbosity_mismatch
- incoherent
- unsafe_or_policy_risk
- pass

Each failure is assigned a severity level: low, medium, or high.

## Outputs
- `reports/llm_audit_report.md`: summarized audit findings and failure analysis
- `results/audits.jsonl`: per-item audit records (generated locally)
- `results/merged_for_analysis.csv`: dataset used for root-cause analysis

## Technologies
- Python
- OpenAI API
- Pandas
- JSON schema validation
- Modular evaluation pipeline design

## Future extensions
- Human-in-the-loop auditor calibration
- Multi-model regression testing
- CI-based quality gates for LLM changes

# Langfuse Prompt A/B Test — Claims Triage

## Purpose

This experiment compares two prompt versions for an insurance claims triage workflow using Langfuse observability.

The objective is to demonstrate prompt versioning, operational tracing, cost visibility and latency comparison for an LLM-based insurance workflow.

## Use Case

A claimant reports water damage discovered after long-term leakage under the kitchen floor and asks whether this is covered.

The workflow should classify the likely claim type, identify missing information and determine whether human review is required.

## Prompt Versions

### v1 — Basic triage prompt

The v1 prompt focuses on basic claim classification and missing information.

### v2 — Governance-aware triage prompt

The v2 prompt adds stronger operational controls:

- Do not confirm or deny coverage
- Identify likely claim type
- Identify missing information
- Flag potential coverage concerns
- State whether human review is required
- Use a concise operational format

## Langfuse Traces

| Field | v1 | v2 |
|---|---:|---:|
| Trace name | `claims-triage-ab-test-v1` | `claims-triage-ab-test-v2` |
| Prompt version | `v1` | `v2` |
| Latency | 4.55s | 5.07s |
| Input tokens | 49 | 77 |
| Output tokens | 139 | 124 |
| Total tokens | 188 | 201 |
| Cost | $0.000091 | $0.000086 |
| Model | `gpt-4o-mini-2024-07-18` | `gpt-4o-mini-2024-07-18` |
| Experiment | `prompt-ab-test` | `prompt-ab-test` |
| Workflow | `claims-triage` | `claims-triage` |
| Use case | `insurance-claims` | `insurance-claims` |

## Observations

Prompt v2 uses more input tokens because it includes additional governance and human-review instructions.

Latency increased slightly from 4.55s to 5.07s.

Total tokens increased from 188 to 201.

The displayed cost remained effectively flat in this small single-run comparison. This should not be overinterpreted as a cost improvement because the sample size is too small.

## Business Interpretation

Prompt v1 is simpler and cheaper to maintain, but less explicit about governance.

Prompt v2 is more suitable for insurance operations because it explicitly avoids confirming coverage and requires human review where coverage may be uncertain.

This is important in regulated insurance workflows because LLM outputs should support triage and decision preparation, not make final coverage decisions without human oversight.

## Interview Positioning

This A/B test demonstrates how prompt changes can be tracked through Langfuse rather than tested informally.

Langfuse captures prompt version, input, output, latency, token usage, cost and metadata.

DeepEval can evaluate whether the output is good. Langfuse shows what happened during the execution and helps compare operational trade-offs across prompt versions.

## Conclusion

Prompt v2 is the preferred version for a governance-aware claims triage workflow because it better aligns with insurance controls, human review and safe automation principles.
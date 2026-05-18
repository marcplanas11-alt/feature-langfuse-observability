from langfuse import Langfuse

langfuse = Langfuse()

claim_text = "Water damage discovered after long-term leakage."

trace = langfuse.trace(
    name="claims-triage-workflow",
    input={"claim": claim_text},
)

generation = trace.generation(
    name="claim-analysis",
    model="gpt-4",
    input=claim_text,
)

response = """
Coverage may be excluded because the wording excludes gradual leakage over time.
Recommend underwriting review.
"""

generation.end(
    output=response
)

trace.update(
    output={"result": response}
)

print("Trace sent to Langfuse successfully.")

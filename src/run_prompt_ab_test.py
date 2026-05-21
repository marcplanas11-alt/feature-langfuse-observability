import os
from dotenv import load_dotenv
from langfuse.openai import openai
from langfuse import get_client

load_dotenv()


def clean_env_value(value: str | None) -> str | None:
    if value is None:
        return None
    return value.strip().strip('"').strip("'")


required_vars = [
    "OPENAI_API_KEY",
    "LANGFUSE_PUBLIC_KEY",
    "LANGFUSE_SECRET_KEY",
]

for var in required_vars:
    value = clean_env_value(os.getenv(var))
    if not value:
        raise RuntimeError(f"Missing required environment variable: {var}")
    os.environ[var] = value

langfuse_url = clean_env_value(
    os.getenv("LANGFUSE_BASE_URL") or os.getenv("LANGFUSE_HOST")
)

if not langfuse_url:
    raise RuntimeError("Missing LANGFUSE_BASE_URL or LANGFUSE_HOST")

os.environ["LANGFUSE_BASE_URL"] = langfuse_url
os.environ["LANGFUSE_HOST"] = langfuse_url


CLAIM_TEXT = (
    "Water damage discovered after long-term leakage under the kitchen floor. "
    "The claimant asks whether this is covered."
)


PROMPTS = {
    "v1": (
        "You are an insurance claims triage assistant. "
        "Classify the claim and identify missing information."
    ),
    "v2": (
        "You are an insurance claims triage assistant. "
        "Do not confirm or deny coverage. "
        "Classify the likely claim type, identify missing information, "
        "flag potential coverage concerns, and state whether human review is required. "
        "Use a concise operational format."
    ),
}


def run_prompt_version(version: str, system_prompt: str) -> None:
    completion = openai.chat.completions.create(
        name=f"claims-triage-ab-test-{version}",
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": CLAIM_TEXT,
            },
        ],
        metadata={
            "workflow": "claims-triage",
            "prompt_version": version,
            "use_case": "insurance-claims",
            "experiment": "prompt-ab-test",
            "environment": "local-dev",
        },
    )

    response = completion.choices[0].message.content

    print("\n" + "=" * 70)
    print(f"PROMPT VERSION: {version}")
    print("=" * 70)
    print(response)
    print("=" * 70)


def main() -> None:
    print("Running Langfuse prompt A/B test...")

    for version, prompt in PROMPTS.items():
        run_prompt_version(version, prompt)

    get_client().flush()

    print("\nA/B test traces sent to Langfuse.")
    print("Open Langfuse → Tracing")
    print("Filter metadata: experiment = prompt-ab-test")
    print("Compare prompt_version = v1 vs v2")


if __name__ == "__main__":
    main()
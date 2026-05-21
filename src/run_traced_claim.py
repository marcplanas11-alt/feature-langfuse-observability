import os
from dotenv import load_dotenv

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

print("Langfuse configuration loaded:")
print(f"- LANGFUSE_BASE_URL: {os.environ['LANGFUSE_BASE_URL']}")
print(f"- LANGFUSE_PUBLIC_KEY: {os.environ['LANGFUSE_PUBLIC_KEY'][:10]}...")


from langfuse.openai import openai
from langfuse import get_client


completion = openai.chat.completions.create(
    name="claims-triage-langfuse-test",
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an insurance claims triage assistant. "
                "Do not confirm coverage. "
                "Identify likely claim type, missing information, "
                "and whether human review is required."
            ),
        },
        {
            "role": "user",
            "content": (
                "Water damage discovered after long-term leakage under the kitchen floor. "
                "The claimant asks whether this is covered."
            ),
        },
    ],
    metadata={
        "workflow": "claims-triage",
        "prompt_version": "v1",
        "use_case": "insurance-claims",
        "environment": "local-dev",
    },
)

response = completion.choices[0].message.content

print("\nCLAIMS TRIAGE RESPONSE")
print("=" * 60)
print(response)
print("=" * 60)

get_client().flush()

print("\nTrace sent to Langfuse.")
print("Open Langfuse Cloud → Project → Traces")
print("Search for: claims-triage-langfuse-test")
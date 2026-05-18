"""
Claims Triage Agent with Langfuse Tracing
Demonstrates best practices for observability with Langfuse and OpenAI
"""

import os
from dotenv import load_dotenv
from langfuse.openai import openai

# Load environment variables BEFORE any Langfuse or OpenAI imports
load_dotenv()

def main():
    """Run the claims triage agent with Langfuse tracing"""
    
    # Initialize OpenAI completion with Langfuse tracing
    # The langfuse.openai wrapper automatically captures:
    # - Model name
    # - Token usage (input/output)
    # - Latency
    # - Model responses
    completion = openai.chat.completions.create(
        name="claims-triage",  # Descriptive trace name
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an insurance claims triage assistant. "
                    "Do not confirm coverage. Identify likely claim type, "
                    "missing information, and whether human review is required."
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
        },
    )

    # Print the response
    response_text = completion.choices[0].message.content
    print("\n" + "="*60)
    print("CLAIMS TRIAGE RESPONSE")
    print("="*60)
    print(response_text)
    print("="*60)
    print("\n✓ Trace sent to Langfuse")
    print("  View your trace at: https://cloud.langfuse.com/traces")

if __name__ == "__main__":
    main()

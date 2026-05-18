# Langfuse Observability Setup

## Prerequisites

1. **Langfuse Account**: Create one at https://cloud.langfuse.com
2. **API Keys**: Get them from Langfuse Settings > API Keys
3. **OpenAI API Key**: Get it from https://platform.openai.com/account/api-keys

## Setup Instructions

### 1. Create `.env` file

Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```

### 2. Edit `.env` with your keys

```
LANGFUSE_PUBLIC_KEY=pk-lf-your-key-here
LANGFUSE_SECRET_KEY=sk-lf-your-key-here
LANGFUSE_HOST=https://cloud.langfuse.com
OPENAI_API_KEY=sk-your-openai-key-here
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the script

```bash
python src/run_traced_claim.py
```

## What Gets Traced Automatically

The Langfuse OpenAI integration captures:

✅ **Model Name** - Which model was used (gpt-4o-mini)
✅ **Token Usage** - Input and output tokens for cost tracking
✅ **Latency** - How long the API call took
✅ **Messages** - Full prompt and response
✅ **Metadata** - Custom tags for filtering (workflow, version, use_case)

## View Your Traces

After running the script, view traces at:
- **Langfuse Dashboard**: https://cloud.langfuse.com/traces
- **Filter by metadata**: workflow="claims-triage"

## Next Steps

1. **Explore the trace** in Langfuse UI
2. **Add user_id** if tracking specific users
3. **Add session_id** for multi-turn conversations
4. **Capture scores** for quality feedback
5. **Build dashboards** to monitor performance over time

## Best Practices Applied

- ✅ Environment variables for credentials (never hardcoded)
- ✅ Descriptive trace names (`claims-triage`)
- ✅ Metadata for organization and filtering
- ✅ Framework integration (automatic instrumentation)
- ✅ Load `.env` before importing Langfuse/OpenAI

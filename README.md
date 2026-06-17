# Langfuse Observability — Claims Triage Trace Demo

Portfolio project showing how to trace a simple insurance claims triage LLM call with Langfuse.

> **Positioning:** this is an observability demo, not a production monitoring platform. It demonstrates local environment loading, trace metadata, model call instrumentation and trace review in Langfuse.

---

## Executive Summary

LLM workflows need observability: prompt, response, model, latency, token usage, cost signals and metadata should be traceable. This repo shows a minimal claims-triage style call instrumented with Langfuse so that each run can be inspected in the Langfuse dashboard.

Workflow:

```text
Local environment config
   ↓
Instrumented OpenAI call through Langfuse
   ↓
Claims triage response
   ↓
Trace flush
   ↓
Langfuse dashboard review
```

---

## Main Files

| File | Purpose |
|---|---|
| `src/run_traced_claim.py` | Loads environment config, runs a traced claims triage model call and flushes the trace |
| `.env.example` | Template showing required local environment variable names |
| `.gitignore` | Prevents local environment files and caches from being committed |
| `requirements.txt` | Python dependencies |

---

## Full Setup and Execution Guide

### 1. Clone the repository

```bash
git clone https://github.com/marcplanas11-alt/feature-langfuse-observability.git
cd feature-langfuse-observability
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Dependencies:

| Package | Use |
|---|---|
| `langfuse` | Trace capture and Langfuse integration |
| `openai` | Model client used by the traced call |
| `python-dotenv` | Loads local environment configuration |

---

## Local Configuration

Create a local `.env` file from the example file:

### Windows CMD

```bash
copy .env.example .env
```

### macOS / Linux

```bash
cp .env.example .env
```

Then edit `.env` locally with your Langfuse and model provider values. Do not commit `.env`.

The script expects these environment variable names:

```text
LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY
LANGFUSE_HOST or LANGFUSE_BASE_URL
OPENAI_API_KEY
```

---

## Run the Trace Demo

```bash
python src/run_traced_claim.py
```

Expected terminal output:

```text
Langfuse configuration loaded:
CLAIMS TRIAGE RESPONSE
Trace sent to Langfuse.
```

Then open Langfuse and search for the trace name:

```text
claims-triage-langfuse-test
```

---

## Complete Command Formula

### Windows CMD

```bash
git clone https://github.com/marcplanas11-alt/feature-langfuse-observability.git
cd feature-langfuse-observability
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python src/run_traced_claim.py
```

### Windows PowerShell

```bash
git clone https://github.com/marcplanas11-alt/feature-langfuse-observability.git
cd feature-langfuse-observability
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python src/run_traced_claim.py
```

### macOS / Linux

```bash
git clone https://github.com/marcplanas11-alt/feature-langfuse-observability.git
cd feature-langfuse-observability
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
python src/run_traced_claim.py
```

---

## What Gets Traced

The trace captures:

- model name;
- input and output messages;
- latency;
- token usage when available;
- metadata such as workflow, prompt version, use case and environment.

---

## Troubleshooting

### Missing environment variable

Edit `.env` and ensure all required variable names are present.

### No trace appears

Check that the local configuration values are correct, then rerun:

```bash
python src/run_traced_claim.py
```

### `.env` appears in Git changes

Do not commit it. `.gitignore` already excludes `.env`.

---

## Cleanup Notes

- `.env.example` belongs in the repo because it is a safe template.
- `.env` must stay local only.
- The script currently runs one hard-coded synthetic claims triage example.
- For a larger portfolio demo, add multiple scenarios and attach scores or feedback to traces.

---

## Author

Built by Marc Planas Callico — Insurance Operations, Business Analysis and AI-enabled transformation.

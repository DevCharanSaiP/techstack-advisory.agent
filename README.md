# Stackwise — Tech Stack Architecture Advisor

A single-agent Streamlit app that recommends a technology stack and a practical architecture from a project brief and optional constraints. It connects to Hugging Face Inference Providers through `huggingface_hub.InferenceClient`.

## Features

- Project type, stage, budget, scale, deployment, availability, team experience, and priorities.
- Optional constraints for languages, frontend, database, storage, integrations, AI/ML, security, and technologies to avoid.
- A focused system prompt that asks for one primary recommendation, trade-offs, cost limitations, risks, and an implementation roadmap.
- Download the recommendation as Markdown.
- Local `.env` support and Streamlit Community Cloud secrets support.
- No database required for the initial version.

## Exact project files

```text
tech_stack_architecture_advisor/
├── app.py
├── prompts.py
├── style.py
├── .env
├── README.md
└── requirements.txt
```

## 1. Prerequisites

- Python 3.10 or newer (use a version supported by Streamlit Community Cloud).
- A Hugging Face account and a user access token with the permissions required by your selected inference provider/model.
- An inference model that is currently available through Hugging Face Inference Providers.

Inference availability, model support, free credits, rate limits, and provider pricing can change. A Hugging Face token authenticates requests; it does not guarantee unlimited or free inference.

## 2. Configure the token

Edit `.env`:

```dotenv
HF_TOKEN=hf_your_actual_token
HF_MODEL=openai/gpt-oss-20b
```

Replace the token placeholder. If the default model is unavailable to your account or provider, change `HF_MODEL` to a chat-completion model currently supported by your Hugging Face account.

**Security:** Never commit a real `.env` or publish your token. This project intentionally contains only the requested files, so be especially careful when staging files for Git. Do not use `git add .` until you have ensured `.env` is excluded. If a token is exposed, revoke it and create a new one.

## 3. Install and run locally

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed in the terminal, usually `http://localhost:8501`.

## 4. Deploy for free on Streamlit Community Cloud

1. Create a GitHub repository containing `app.py`, `prompts.py`, `style.py`, `README.md`, and `requirements.txt`.
2. Do **not** upload the real `.env`. Keep it local.
3. Push the safe project files to GitHub.
4. Open [Streamlit Community Cloud](https://share.streamlit.io/) and create an app from the repository, selecting `app.py` as the entrypoint.
5. In the app's Advanced settings / Secrets field, add:

   ```toml
   HF_TOKEN = "hf_your_actual_token"
   HF_MODEL = "openai/gpt-oss-20b"
   ```

6. Deploy and test with a non-sensitive project brief.

Streamlit Community Cloud can sleep or have resource limitations. Hugging Face inference can also have quotas, provider/model availability constraints, or paid usage. Free deployment does not mean unlimited uptime or unlimited inference.

## 5. Troubleshooting

- **401 / 403:** Check the token, model access, and provider permissions.
- **Model not supported / no provider:** Choose a model currently supported by Hugging Face Inference Providers.
- **Rate limit / quota:** Wait for quota reset or select an available provider/model. Do not assume a paid fallback is free.
- **Empty or poor recommendations:** Give a more specific project brief, reduce conflicting constraints, or choose a model with stronger instruction-following ability.
- **Deployment can't find a package:** Check `requirements.txt` and the build logs.

## Architecture

`app.py` collects inputs and calls Hugging Face. `prompts.py` holds the advisor's system prompt and formats the brief. `style.py` contains presentation styling. The first version is a single LLM-powered advisor, not a multi-agent system and not a verified cloud-cost calculator.

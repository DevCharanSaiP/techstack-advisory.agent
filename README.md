# Stackwise — Tech Stack Architecture Advisor

Stackwise is a Streamlit app that turns a project brief and technical constraints into a practical technology-stack and architecture recommendation. It uses Google's Gemini API through the `google-genai` Python SDK.

## What it does

- Collects a project description and context such as application type, budget, expected scale, project stage, team experience, deployment preference, availability needs, and priorities.
- Accepts optional constraints for languages, frontend, database, storage, integrations, AI/ML, security/compliance, and technologies to avoid.
- Sends the brief to Gemini with an architecture-focused prompt designed to return a primary recommendation, trade-offs and risks, an implementation roadmap, alternatives, and open questions.
- Displays the generated recommendation and lets you download it as a Markdown file.
- Supports a configurable Gemini model ID. The default is `gemini-2.5-flash`; model availability and account quotas may vary.

Recommendations are decision support, not verified cost estimates, security reviews, compliance assessments, or load tests.

## Project files

```text
.
├── app.py           # Streamlit interface and Gemini API calls
├── prompts.py       # System prompt and project-brief formatting
├── style.py         # App styling
├── checkmodels.py   # Optional Gemini model-listing utility
├── requirements.txt
└── README.md
```

Local configuration such as `.env`, virtual environments, and Python cache files is excluded from Git.

## Requirements

- Python 3.10 or newer, using a version supported by the current Streamlit and Google Gen AI SDK releases.
- A Google AI Studio API key with access to the Gemini API.
- Internet access while running the app.

Gemini model access, quotas, pricing, and free-tier availability can change. Check the current Google AI Studio documentation and account limits before relying on a model or cost assumption.

## Run locally

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure credentials

Create a `.env` file in the project root:

```dotenv
GOOGLE_API_KEY=your_google_ai_studio_api_key
GEMINI_MODEL=gemini-2.5-flash
```

`GOOGLE_API_KEY` is required. `GEMINI_MODEL` is optional; when omitted, the app uses `gemini-2.5-flash`. You can also change the model ID in the app's sidebar.

Never commit or share a real API key. Keep `.env` local; the repository's `.gitignore` excludes it. If a key is exposed, revoke it and create a replacement.

### 4. Start the app

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push the project files to a GitHub repository. Do not upload `.env`.
2. Create a Streamlit Community Cloud app connected to the repository and select `app.py` as the entry point.
3. Add the following in the app's **Secrets** settings, replacing the example key:

   ```toml
   GOOGLE_API_KEY = "your_google_ai_studio_api_key"
   GEMINI_MODEL = "gemini-2.5-flash"
   ```

The app prefers Streamlit deployment secrets when available and otherwise reads local environment variables loaded from `.env`. Deployment secrets are not stored in the repository.

## Optional: list available models

With `GOOGLE_API_KEY` set in the environment or in the root `.env`, run:

```bash
python checkmodels.py
```

The script lists models that advertise `generateContent` support for the configured key. It is a diagnostic aid; availability can change, and the app may still be subject to model-specific permissions or quotas.

## Privacy and troubleshooting

The project brief is sent to Google's Gemini API to generate a recommendation. Do not submit passwords, API keys, credentials, personal data, or confidential information.

- **API key not configured:** Set `GOOGLE_API_KEY` in `.env` for local use or Streamlit secrets for deployment.
- **Authentication error (401):** Check that the key is valid and belongs to the intended Google AI Studio account.
- **Access error (403):** Check model access, API permissions, and account or regional restrictions.
- **Quota or rate-limit error (429):** Review current account/model limits and try again when permitted.
- **Model not found or unavailable:** Verify the model ID and that it is available to your API key; choose another supported ID in the sidebar.
- **Timeout:** Retry or shorten the project description.

## How recommendations are formed

`app.py` collects the form values, constructs a project brief, and calls the Gemini API. `prompts.py` supplies the system instructions and formats the brief. `style.py` applies the interface styling. The app generates one model response per submission; it is not a multi-agent system or an automated architecture-validation service.

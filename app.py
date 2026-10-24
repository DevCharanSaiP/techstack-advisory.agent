
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import SYSTEM_PROMPT, build_user_prompt
from style import apply_styles


# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv()

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

st.set_page_config(
    page_title="Stackwise — Tech Stack Advisor",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def get_deployment_secrets():
    """Read Streamlit deployment secrets without breaking local execution."""
    try:
        api_key = str(st.secrets.get("GOOGLE_API_KEY", "")).strip()
        model = str(st.secrets.get("GEMINI_MODEL", "")).strip()
        return api_key, model
    except Exception:
        return "", ""


def get_api_key():
    """Prefer deployment secrets, then fall back to local .env."""
    deployment_key, _ = get_deployment_secrets()
    local_key = os.getenv("GOOGLE_API_KEY", "").strip()
    return deployment_key or local_key


def get_model_default():
    """Resolve the model from deployment secrets or local configuration."""
    _, deployment_model = get_deployment_secrets()
    return deployment_model or DEFAULT_MODEL


def generate_recommendation(api_key, model, user_prompt):
    """Generate an architecture recommendation using the Gemini API."""
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.25,
            max_output_tokens=2200,
        ),
    )

    answer = response.text

    if not answer or not answer.strip():
        raise ValueError(
            "Gemini returned an empty response. The request may have been "
            "blocked, or the selected model may not have generated text."
        )

    return answer.strip()


# --------------------------------------------------
# Application header
# --------------------------------------------------

st.title("Stackwise")
st.caption(
    "A practical architecture advisor for choosing a technology "
    "stack that fits your constraints."
)

st.markdown(
    "Describe what you're building. Add only the constraints you know; "
    "the advisor will distinguish assumptions from requirements."
)


# --------------------------------------------------
# Sidebar: model configuration
# --------------------------------------------------

with st.sidebar:
    st.header("Model connection")

    api_key = get_api_key()
    model_default = get_model_default()

    model = st.text_input(
        "Gemini model ID",
        value=model_default,
        help=(
            "Enter a model ID currently available to your Google AI Studio "
            "API key. Free-tier availability and quotas vary by model."
        ),
    ).strip()

    if api_key:
        st.success("API key detected")
    else:
        st.warning("Gemini API key not configured")

    st.caption(
        "The API key is read from your local .env file or "
        "Streamlit Community Cloud secrets."
    )

    st.divider()

    st.markdown("**Privacy note**")
    st.caption(
        "Your project details are sent to Google's Gemini API to generate "
        "the recommendation. Do not submit passwords, API keys, credentials, "
        "or confidential company information."
    )

    with st.expander("Configuration help"):
        st.markdown(
            """
            **Local `.env`:**

            ```dotenv
            GOOGLE_API_KEY=your_gemini_api_key
            GEMINI_MODEL=gemini-2.5-flash
            ```

            **Deployment secrets:**

            ```toml
            GOOGLE_API_KEY = "your_gemini_api_key"
            GEMINI_MODEL = "gemini-2.5-flash"
            ```
            """
        )


# --------------------------------------------------
# Project brief form
# --------------------------------------------------

with st.form("architecture_form"):
    st.subheader("Project brief")

    project_name = st.text_input(
        "Project name (optional)",
        placeholder="e.g., AnylR analytics platform",
    )

    project_description = st.text_area(
        "What are you building?",
        placeholder=(
            "Explain the product, users, core workflows, "
            "and the problem it solves..."
        ),
        height=140,
    )

    col_a, col_b = st.columns(2)

    with col_a:
        project_type = st.selectbox(
            "Application type",
            [
                "Not sure / recommend",
                "SaaS / web app",
                "API / backend service",
                "AI / ML application",
                "Data platform / analytics",
                "Mobile app",
                "Internal enterprise tool",
                "IoT / edge system",
                "Developer tool",
                "Other",
            ],
        )

        deployment = st.selectbox(
            "Deployment preference",
            [
                "Recommend the best fit",
                "Free tier / $0 prototype",
                "Serverless",
                "AWS",
                "Azure",
                "Google Cloud",
                "Cloud-agnostic",
                "On-premises / self-hosted",
                "Vercel / Netlify-style platform",
            ],
        )

        budget = st.selectbox(
            "Budget",
            [
                "Strictly ₹0 / free tiers only",
                "Minimal cost",
                "Moderate budget",
                "Enterprise budget",
                "Not decided",
            ],
        )

        scale = st.selectbox(
            "Expected scale",
            [
                "Unknown / estimate for me",
                "Prototype / personal use",
                "Up to 1,000 users",
                "1,000–100,000 users",
                "100,000+ users",
                "High-throughput internal system",
            ],
        )

    with col_b:
        stage = st.selectbox(
            "Project stage",
            [
                "Idea",
                "MVP",
                "Production",
                "Scaling / redesign",
            ],
        )

        team = st.selectbox(
            "Team experience",
            [
                "Solo developer",
                "Small team / generalist",
                "Experienced engineering team",
                "Enterprise / multiple teams",
            ],
        )

        priority = st.multiselect(
            "Top priorities (choose any)",
            [
                "Fastest to build",
                "Lowest operating cost",
                "Performance",
                "Scalability",
                "Security / compliance",
                "Developer experience",
                "Low maintenance",
                "Portability / avoid lock-in",
                "Open source",
                "AI / ML capability",
            ],
            default=[
                "Lowest operating cost",
                "Fastest to build",
            ],
        )

        availability = st.selectbox(
            "Availability needs",
            [
                "Best effort is fine",
                "Reliable production service",
                "High availability / mission-critical",
            ],
        )

    with st.expander(
        "Optional technical constraints",
        expanded=True,
    ):
        col_c, col_d = st.columns(2)

        with col_c:
            languages = st.text_input(
                "Preferred languages",
                placeholder="e.g., Python, TypeScript",
            )

            frontend = st.text_input(
                "Frontend constraints",
                placeholder="e.g., React, mobile-first",
            )

            data = st.text_input(
                "Data and storage needs",
                placeholder="e.g., relational, files, vector search",
            )

            integrations = st.text_input(
                "Required integrations",
                placeholder="e.g., Stripe, Slack, AWS services",
            )

        with col_d:
            database = st.text_input(
                "Database preference",
                placeholder="e.g., PostgreSQL, DynamoDB",
            )

            ai_needs = st.text_input(
                "AI / ML needs",
                placeholder="e.g., RAG, agents, inference, training",
            )

            security = st.text_input(
                "Security / compliance",
                placeholder="e.g., PII, encryption, RBAC, GDPR",
            )

            avoid = st.text_input(
                "Technologies to avoid",
                placeholder="e.g., Kubernetes, paid APIs, Java",
            )

    extra = st.text_area(
        "Anything else? (optional)",
        placeholder=(
            "Known requirements, deployment region, team skills, "
            "or trade-offs..."
        ),
        height=90,
    )

    submitted = st.form_submit_button(
        "Generate architecture recommendation",
        type="primary",
        use_container_width=True,
    )


# --------------------------------------------------
# Generate recommendation
# --------------------------------------------------

if submitted:
    if not project_description.strip():
        st.error(
            "Please describe what you're building so the advisor "
            "can make a useful recommendation."
        )

    elif not api_key:
        st.error(
            "Gemini API key not found. Configure GOOGLE_API_KEY "
            "in your local .env file or deployment secrets."
        )

        st.code(
            "GOOGLE_API_KEY=your_gemini_api_key\n"
            "GEMINI_MODEL=gemini-2.5-flash",
            language="dotenv",
        )

        st.markdown(
            "[Get an API key from Google AI Studio]"
            "(https://aistudio.google.com/apikey)"
        )

    elif not model:
        st.error("Please enter a Gemini model ID.")

    else:
        brief = {
            "project_name": project_name or "Not provided",
            "project_description": project_description,
            "application_type": project_type,
            "deployment_preference": deployment,
            "budget": budget,
            "expected_scale": scale,
            "project_stage": stage,
            "team_experience": team,
            "priorities": priority or ["Not specified"],
            "availability": availability,
            "preferred_languages": languages or "Not specified",
            "frontend_constraints": frontend or "Not specified",
            "data_storage_needs": data or "Not specified",
            "required_integrations": integrations or "Not specified",
            "database_preference": database or "Not specified",
            "ai_ml_needs": ai_needs or "Not specified",
            "security_compliance": security or "Not specified",
            "technologies_to_avoid": avoid or "Not specified",
            "additional_context": extra or "Not provided",
        }

        user_prompt = build_user_prompt(brief)

        try:
            with st.spinner(
                "Evaluating constraints and generating your architecture..."
            ):
                answer = generate_recommendation(
                    api_key=api_key,
                    model=model,
                    user_prompt=user_prompt,
                )

            st.session_state["last_answer"] = answer
            st.session_state["last_brief"] = brief
            st.session_state["last_model"] = model

        except Exception as exc:
            error_text = str(exc)
            error_lower = error_text.lower()

            st.error("Gemini could not generate the recommendation.")

            if (
                "api_key_invalid" in error_lower
                or "api key not valid" in error_lower
                or "unauthenticated" in error_lower
                or "401" in error_text
            ):
                st.warning(
                    "Authentication failed. Verify your API key in "
                    "Google AI Studio and ensure the correct key is configured."
                )

            elif (
                "permission_denied" in error_lower
                or "403" in error_text
            ):
                st.warning(
                    "Access was denied. Check model availability, API "
                    "permissions, and any account or regional restrictions."
                )

            elif (
                "resource_exhausted" in error_lower
                or "429" in error_text
                or "quota" in error_lower
            ):
                st.warning(
                    "The model's rate limit or quota may have been reached. "
                    "Check your Google AI Studio usage and the selected "
                    "model's current free-tier limits before retrying."
                )

            elif (
                "not_found" in error_lower
                or "404" in error_text
                or "model" in error_lower
            ):
                st.warning(
                    "The selected model may be unavailable or unsupported "
                    "for your API key. Check the current Gemini API model list "
                    "and try an available model ID."
                )

            elif (
                "deadline_exceeded" in error_lower
                or "timeout" in error_lower
            ):
                st.warning(
                    "The request timed out. Try again or use a shorter "
                    "project description."
                )

            else:
                st.warning(
                    "Check your internet connection, Gemini API availability, "
                    "model configuration, and account quota."
                )

            with st.expander("Technical error details"):
                st.code(
                    f"{type(exc).__name__}: {error_text}"
                )


# --------------------------------------------------
# Display recommendation
# --------------------------------------------------

if st.session_state.get("last_answer"):
    st.divider()

    st.subheader("Your architecture recommendation")

    last_model = st.session_state.get(
        "last_model",
        "Unknown",
    )

    st.caption(f"Generated using Gemini model: {last_model}")

    st.markdown(
        st.session_state["last_answer"]
    )

    st.download_button(
        "Download recommendation as Markdown",
        data=st.session_state["last_answer"],
        file_name="tech_stack_architecture_recommendation.md",
        mime="text/markdown",
    )

    with st.expander("View the constraints used"):
        st.json(
            st.session_state.get("last_brief", {})
        )

st.divider()

st.caption(
    "Stackwise provides decision support, not a substitute for "
    "security review, load testing, compliance assessment, or a "
    "verified cost estimate."
)

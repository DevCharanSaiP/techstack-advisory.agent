import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        :root {
            --advisor-accent: #7c6cff;
        }
        .stApp {
            background:
                radial-gradient(ellipse at 12% 0%, rgba(124,108,255,0.10), transparent 38%),
                var(--background-color);
        }
        .block-container {
            max-width: 1180px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }
        h1 {
            letter-spacing: -0.045em;
            font-weight: 800 !important;
        }
        h2, h3 {
            letter-spacing: -0.025em;
        }
        [data-testid="stForm"] {
            border: 1px solid rgba(128,128,128,0.24);
            border-radius: 16px;
            padding: 1.25rem;
            background: rgba(128,128,128,0.035);
        }
        div.stButton > button[kind="primary"],
        div.stFormSubmitButton > button[kind="primary"] {
            border: 0;
            border-radius: 10px;
            font-weight: 700;
            min-height: 2.8rem;
        }
        [data-testid="stMetric"] {
            border: 1px solid rgba(128,128,128,0.2);
            padding: 0.75rem;
            border-radius: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import gradio as gr

from prompts import SYSTEM_PROMPT, build_user_prompt
from style import CSS

# ---- Load token and set up client ----
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN,
)

# ---- Core generation function ----
def generate_architecture(project_description, size, users, budget,
                          experience, preferences, priorities, extra_constraints):
    if not project_description.strip():
        return "Please provide a project description first."

    user_prompt = build_user_prompt(
        project_description, size, users, budget,
        experience, preferences, priorities, extra_constraints
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=1200,
        temperature=0.9,
    )

    return response.choices[0].message["content"]


# ---- Gradio UI ----
with gr.Blocks() as demo:
    gr.HTML(
        CSS
        + """
        <div id="title-wrap">
          <h1>Tech Stack Architecture Advisor</h1>
          <p>Describe your project and constraints. Get structured, comparative tech stack suggestions.</p>
        </div>
        """
    )

    with gr.Column(elem_classes=["panel"]):
        project_description = gr.Textbox(
            label="Project description",
            placeholder="Describe what you want to build (features, target users, rough scope)...",
            lines=5,
        )

        with gr.Row():
            size = gr.Dropdown(
                ["Small MVP", "Medium product", "Large / Enterprise"],
                label="Project size",
                value="Small MVP",
            )
            users = gr.Dropdown(
                ["Internal tool", "Consumer app", "B2B / SaaS", "Open-source project"],
                label="Target users",
                value="B2B / SaaS",
            )
            budget = gr.Dropdown(
                ["Zero / Hobby", "Low", "Moderate", "Flexible"],
                label="Budget",
                value="Low",
            )

        with gr.Row():
            experience = gr.Dropdown(
                ["Beginner", "Intermediate", "Advanced / Mixed"],
                label="Team experience",
                value="Intermediate",
            )
            priorities = gr.Textbox(
                label="Main priorities",
                placeholder="e.g., Time-to-market, scalability, low cost, DX, performance...",
                lines=1,
            )
            preferences = gr.Textbox(
                label="Tech preferences (likes / dislikes)",
                placeholder="e.g., Prefer JS + Python, avoid Java; cloud preference, etc.",
                lines=1,
            )

        extra_constraints = gr.Textbox(
            label="Extra constraints / context (optional)",
            placeholder="e.g., Must be open-source only, must run on-prem, strict data privacy, specific integrations...",
            lines=2,
        )

        generate_button = gr.Button("Generate Architecture Plan", variant="primary")

        output = gr.Markdown(
            label="Recommended architecture",
            elem_classes=["arch-output"],
            value="Your architecture summary and tables will appear here."
        )

        generate_button.click(
            fn=generate_architecture,
            inputs=[
                project_description,
                size,
                users,
                budget,
                experience,
                preferences,
                priorities,
                extra_constraints,
            ],
            outputs=output,
        )


if __name__ == "__main__":
    demo.launch()
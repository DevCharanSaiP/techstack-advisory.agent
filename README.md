# Tech Stack Architecture Advisor

An AI-powered tool that provides structured, comparative tech stack recommendations based on your project requirements and constraints.

## Overview

The Tech Stack Architecture Advisor uses a large language model (LLaMA 3.8B via HuggingFace Inference API) to generate tailored technology stack recommendations. Simply describe your project, specify your constraints, and receive detailed layer-by-layer architecture suggestions with pros and cons for each option.

## Features

- **AI-Driven Recommendations**: Uses Meta's LLaMA 3.8B model for intelligent tech stack suggestions
- **Project Context**: Considers project size, target users, budget, team experience, and specific constraints
- **Layer-by-Layer Analysis**: Provides recommendations across frontend, backend, database, authentication, hosting, and more
- **Comparative Tables**: Shows multiple options with pros/cons for each architectural layer
- **Customizable Constraints**: Input tech preferences, priorities, and specific requirements
- **Beautiful UI**: Modern, accessible web interface built with Gradio featuring dark/light theme support

## Quick Start

### Prerequisites

- Python 3.8+
- HuggingFace API token (get one at [huggingface.co](https://huggingface.co))

### Installation

1. **Clone or download the project**

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   HUGGINGFACE_API_TOKEN=your_token_here
   ```

### Running the Application

```bash
python app.py
```

The application will launch at `http://localhost:7860` (default Gradio port).

## Usage

1. **Describe your project**: Provide a detailed description of what you want to build, including features and scope
2. **Select project parameters**:
   - **Project Size**: Small MVP, Medium product, or Large/Enterprise
   - **Target Users**: Internal tool, Consumer app, B2B/SaaS, or Open-source project
   - **Budget**: Zero/Hobby, Low, Moderate, or Flexible
   - **Team Experience**: Beginner, Intermediate, or Advanced/Mixed
3. **Specify preferences** (optional):
   - **Tech Preferences**: Languages, frameworks you like or want to avoid
   - **Main Priorities**: Factors like time-to-market, scalability, cost, developer experience
   - **Extra Constraints**: Special requirements like open-source only, on-premises, data privacy needs
4. **Generate Architecture**: Click the submit button to get AI-powered recommendations

## Project Structure

```
TechStack_Advisor/
├── app.py              # Main Gradio application and UI
├── prompts.py          # System prompt and user prompt builder
├── style.py            # CSS styling for the web interface
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create this with your API token)
└── README.md          # This file
```

## Files Description

### `app.py`
- Main application file that sets up the Gradio web interface
- Integrates with HuggingFace Inference API for LLM generation
- Handles user inputs and displays AI recommendations
- Configures UI components and layout

### `prompts.py`
- Contains the system prompt that defines the AI's behavior
- Includes structured instructions for tech stack analysis
- Provides `build_user_prompt()` function to construct prompts from user inputs

### `style.py`
- CSS styling for the Gradio interface
- Features theme-aware design with light and dark mode support
- Uses modern, accessible design patterns
- Responsive layout for various screen sizes

### `requirements.txt`
- `gradio==6.0.2`: Web UI framework
- `huggingface_hub`: HuggingFace API client
- `python-dotenv`: Environment variable management

## Configuration

### API Configuration
- **Model**: Meta-Llama/Meta-Llama-3-8B-Instruct
- **Max Tokens**: 1200
- **Temperature**: 0.9 (for creative but coherent suggestions)

### Output Format
The AI generates recommendations in this structure:
- High-level summary (3-5 bullet points)
- Layer-by-layer comparative tables with:
  - Layer name
  - Technology options
  - Pros and cons for each option
  - Recommendation status (Highly Recommended/Alternate)

## Environment Variables

Create a `.env` file with:
```
HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here
```

Get your token from [HuggingFace Settings](https://huggingface.co/settings/tokens)

## Dependencies

- **gradio**: Interactive web interface framework
- **huggingface_hub**: Python client for HuggingFace Inference API
- **python-dotenv**: Load environment variables from .env files

## Troubleshooting

### "API token not found"
- Ensure your `.env` file exists and contains a valid `HUGGINGFACE_API_TOKEN`
- Check that the token is active in your HuggingFace account settings

### "Empty response from model"
- Ensure your project description is detailed enough
- Check your API token has active quota/credits
- Verify internet connection to HuggingFace API

### UI styling issues
- Clear your browser cache
- Try a different browser or incognito mode
- Ensure you're using a modern browser (Chrome, Firefox, Safari, Edge)

## How It Works

1. User provides project details through the Gradio interface
2. System combines system prompt + user inputs into a structured message
3. HuggingFace Inference API processes the request using LLaMA 3.8B
4. AI generates comparative tech stack recommendations
5. Formatted markdown output displays in the UI

## Limitations

- Responses are generated with temperature 0.9, so outputs may vary
- Maximum token length is 1200, limiting very detailed responses
- Requires active internet connection and valid HuggingFace API token
- API rate limits apply based on your HuggingFace plan

## License

This project is open source. Feel free to modify and use as needed.

## Contributing

To improve this project:
1. Enhance the system prompt for better recommendations
2. Add more UI customization options
3. Implement caching for similar queries
4. Add support for multiple LLM models
5. Improve styling and accessibility

## Notes

- The AI provides suggestions based on general best practices; always validate recommendations for your specific needs
- This tool is designed to assist decision-making, not replace expert judgment
- Consider running a pilot or proof-of-concept before full technology adoption

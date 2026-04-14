# LLM Resume Analyzer

An end-to-end GenAI project that compares a resume against a job description and returns ATS-style insights such as match score, missing keywords, strengths, improvement areas, and a tailored professional summary.

## Features
- Upload resume files in PDF, DOCX, or TXT format
- ATS-style score generation
- Missing keyword detection
- Strengths and improvement suggestions
- Tailored summary generation
- FastAPI backend
- Streamlit UI
- Downloadable JSON analysis report
- OpenRouter-compatible LLM support

## Tech Stack
- Python
- FastAPI
- Streamlit
- Prompt Engineering
- NLP
- LLM Integration
- REST API
- Pydantic
- Requests
- Pytest

## Project Structure
```text
llm-resume-analyzer/
├── app/
├── tests/
├── sample_data/
├── outputs/
├── screenshots/
├── .github/workflows/
├── streamlit_app.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
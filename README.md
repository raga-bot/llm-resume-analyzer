# LLM Resume Analyzer

A recruiter-ready GenAI project that compares a resume against a job description and returns ATS-style insights such as match score, missing keywords, strengths, improvement areas, and a tailored professional summary.

## Features
- Resume vs Job Description analysis
- ATS-style score generation
- Missing keyword extraction
- Tailored summary generation
- FastAPI backend
- Prompt engineering workflow
- OpenAI-compatible API support
- Sample outputs for recruiter review

## Tech Stack
- Python
- FastAPI
- Prompt Engineering
- LLM Integration
- REST API
- Pydantic
- Requests

## Project Structure
```text
llm-resume-analyzer/
├── app/
├── tests/
├── sample_data/
├── outputs/
├── .github/workflows/
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/llm-resume-analyzer.git
cd llm-resume-analyzer
python -m venv .venv
```

### Activate environment
Windows:
```bash
.venv\Scripts\activate
```

Mac/Linux:
```bash
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configure environment
Copy `.env.example` to `.env` and set your API key.

### Run the app
```bash
uvicorn app.main:app --reload
```

Open:
- API docs: `http://127.0.0.1:8000/docs`
- Health endpoint: `http://127.0.0.1:8000/health`

## Sample API Request
POST `/analyze`
```json
{
  "resume_text": "Computer Science undergraduate with strong foundations in Python, SQL, machine learning, NLP, and building predictive models...",
  "job_description": "We are hiring a GenAI / Python Developer with experience in Python, NLP, LLM workflows, prompt engineering..."
}
```

## Sample Output
See:
- `outputs/sample_response.json`
- `outputs/sample_summary.txt`

## Resume Bullet
Developed an LLM-powered Resume Analyzer using FastAPI and OpenAI-compatible APIs to evaluate resumes against job descriptions, generate ATS-style match scores, identify missing keywords, and produce tailored professional summaries.

## Future Enhancements
- PDF/DOCX resume parsing
- Streamlit or React frontend
- Embeddings-based retrieval
- Candidate comparison dashboard

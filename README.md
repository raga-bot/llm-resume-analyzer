# LLM Resume Analyzer (GenAI Project)

## Overview
The LLM Resume Analyzer is a Generative AI-powered application that evaluates a candidate’s resume against a job description and provides ATS-style insights.

It uses Large Language Models (LLMs) to simulate how recruiters and ATS systems assess resumes and helps improve resume quality for better shortlisting.

## Key Features
- ATS match score generation (0–100)
- Missing keyword identification
- Strengths and improvement suggestions
- AI-generated tailored resume summary
- FastAPI-based REST API
- Structured JSON output
- Sample outputs included

## Tech Stack
- Python  
- FastAPI  
- OpenAI-compatible APIs  
- Prompt Engineering  
- Pydantic  
- Requests  
- Pytest   

## How It Works

1. Input resume text and job description  
2. LLM analyzes the content  
3. Generates structured ATS insights  
4. Returns JSON output including score and suggestions  

## API Endpoints

GET /health  
POST /analyze  

## Request

{
  "resume_text": "Your resume content...",
  "job_description": "Job description content..."
}

## Output

Check:
outputs/sample_response.json  
outputs/sample_summary.txt  

## Use Case

- Resume screening automation  
- ATS optimization  
- Recruitment support tools  
- GenAI-based text analysis  

## Author
Besta Sudha Ragavarshini 
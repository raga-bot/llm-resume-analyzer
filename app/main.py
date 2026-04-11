from fastapi import FastAPI, HTTPException
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.llm import LLMClient
from app.utils import extract_json

app = FastAPI(
    title="LLM Resume Analyzer",
    version="1.0.0",
    description="Analyze resumes against job descriptions using an LLM."
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    try:
        client = LLMClient()
        raw_output = client.analyze_resume(
            resume_text=request.resume_text,
            job_description=request.job_description
        )

        parsed = extract_json(raw_output)

        return AnalyzeResponse(
            score=int(parsed.get("score", 0)),
            missing_keywords=list(parsed.get("missing_keywords", [])),
            strengths=list(parsed.get("strengths", [])),
            improvements=list(parsed.get("improvements", [])),
            tailored_summary=str(parsed.get("tailored_summary", "")),
            raw_llm_output=raw_output,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

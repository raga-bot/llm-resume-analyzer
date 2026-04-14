import json

from fastapi import FastAPI, HTTPException

from app.llm import LLMClient
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.scoring import keyword_overlap_score, combine_scores
from app.utils import extract_json

app = FastAPI(
    title="LLM Resume Analyzer",
    version="2.0.0",
    description="Analyze resumes against job descriptions using an LLM.",
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
            job_description=request.job_description,
        )

        parsed = extract_json(raw_output)

        llm_score = int(parsed.get("score", 0))
        keyword_score, keyword_missing = keyword_overlap_score(
            request.resume_text,
            request.job_description,
        )
        final_score = combine_scores(llm_score, keyword_score)

        existing_missing = list(parsed.get("missing_keywords", []))
        merged_missing = existing_missing[:]
        for item in keyword_missing:
            if item not in merged_missing:
                merged_missing.append(item)

        cleaned_output = json.dumps(parsed, indent=2)

        return AnalyzeResponse(
            score=final_score,
            missing_keywords=merged_missing[:10],
            strengths=list(parsed.get("strengths", [])),
            improvements=list(parsed.get("improvements", [])),
            tailored_summary=str(parsed.get("tailored_summary", "")),
            raw_llm_output=cleaned_output,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
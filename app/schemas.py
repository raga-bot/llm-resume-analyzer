from pydantic import BaseModel, Field
from typing import List


class AnalyzeRequest(BaseModel):
    resume_text: str = Field(..., min_length=50)
    job_description: str = Field(..., min_length=50)


class AnalyzeResponse(BaseModel):
    score: int
    missing_keywords: List[str]
    strengths: List[str]
    improvements: List[str]
    tailored_summary: str
    raw_llm_output: str

import os

import requests
from dotenv import load_dotenv

from app.prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter")
LLM_MODEL = os.getenv("LLM_MODEL", "openrouter/auto")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")


class LLMClient:
    def __init__(self) -> None:
        if not LLM_API_KEY:
            raise ValueError("LLM_API_KEY is not set.")
        self.provider = LLM_PROVIDER
        self.model = LLM_MODEL
        self.api_key = LLM_API_KEY
        self.base_url = LLM_BASE_URL.rstrip("/")

    def analyze_resume(self, resume_text: str, job_description: str) -> str:
        url = f"{self.base_url}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if self.provider == "openrouter":
            headers["HTTP-Referer"] = "https://github.com/raga-bot/llm-resume-analyzer"
            headers["X-Title"] = "LLM Resume Analyzer"

        payload = {
            "model": self.model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": build_user_prompt(
                        resume_text=resume_text,
                        job_description=job_description,
                    ),
                },
            ],
        }

        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
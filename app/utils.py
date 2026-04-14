import json
import re
from typing import Any, Dict


def extract_json(text: str) -> Dict[str, Any]:
    """
    Extracts JSON from LLM output.
    Handles cases where JSON is wrapped in markdown code blocks.
    """

    if not text:
        raise ValueError("Empty response from LLM.")

    text = text.strip()

    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No valid JSON found in LLM response.")

    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse extracted JSON: {str(e)}")
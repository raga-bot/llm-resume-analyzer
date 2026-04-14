from app.utils import extract_json


def test_extract_json_with_code_fence():
    text = """```json
    {
      "score": 80,
      "missing_keywords": ["api"],
      "strengths": ["python"],
      "improvements": ["add projects"],
      "tailored_summary": "Good fit"
    }
    ```"""
    parsed = extract_json(text)
    assert parsed["score"] == 80
    assert parsed["missing_keywords"] == ["api"]
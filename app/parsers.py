from pathlib import Path
from io import BytesIO

from pypdf import PdfReader
from docx import Document


def parse_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="ignore").strip()


def parse_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(BytesIO(file_bytes))
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)
    return "\n".join(pages).strip()


def parse_docx(file_bytes: bytes) -> str:
    document = Document(BytesIO(file_bytes))
    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
    return "\n".join(paragraphs).strip()


def parse_file(filename: str, file_bytes: bytes) -> str:
    suffix = Path(filename).suffix.lower()

    if suffix == ".txt":
        return parse_txt(file_bytes)
    if suffix == ".pdf":
        return parse_pdf(file_bytes)
    if suffix == ".docx":
        return parse_docx(file_bytes)

    raise ValueError("Unsupported file format. Please upload PDF, DOCX, or TXT.")


def parse_resume_file(filename: str, file_bytes: bytes) -> str:
    return parse_file(filename, file_bytes)


def parse_job_description_file(filename: str, file_bytes: bytes) -> str:
    return parse_file(filename, file_bytes)
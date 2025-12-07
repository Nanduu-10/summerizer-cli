import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document
from pathlib import Path

def load_text_from_file(path: str) -> str:
    p = Path(path)
    ext = p.suffix.lower()
    if ext in {".txt", ".md"}:
        return p.read_text(encoding="utf-8", errors="ignore")
    if ext == ".pdf":
        return pdf_extract_text(str(p))
    if ext == ".docx":
        doc = Document(str(p))
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    raise ValueError("Unsupported file type")

def load_text_from_url(url: str) -> str:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]): tag.decompose()
    return soup.get_text(separator="\n")
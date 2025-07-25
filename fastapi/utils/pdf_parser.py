import pdfplumber
from fastapi import UploadFile

from utils.scorer import compute_score
from utils.summarizer import summarize
from utils.resume_utils import extract_details
def extract_text_from_pdf(file):
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text  




async def process_resume(file: UploadFile, jd: str):
    try:
        text = extract_text_from_pdf(file)
        score = compute_score(text, jd)
        summary = summarize(text)
        contact_info = extract_details(text)

        return {
            "filename": file.filename,
            "score": score,
            "summary": summary,
            "name": contact_info["name"],
            "email": contact_info["email"],
            "phone": contact_info["phone"],
        }
    except Exception as e:
        return {
            "filename": file.filename,
            "error": f"Failed to process: {str(e)}"
        }

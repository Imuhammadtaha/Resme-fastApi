from fastapi import FastAPI, UploadFile, Form, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.pdf_parser import process_resume
from typing import List
import asyncio
import en_core_web_sm  # Optimized model import

nlp = en_core_web_sm.load()  # No runtime download!

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/score-resumes")
async def score_multiple_resumes(
    files: List[UploadFile] = File(...),
    jd: str = Form(...)
):
    tasks = []
    for file in files:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail=f"{file.filename} is not a PDF")
        tasks.append(process_resume(file, jd))
    
    results = await asyncio.gather(*tasks)

    return {
        "results": results
    }

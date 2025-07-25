from fastapi import FastAPI,UploadFile,Form,File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.pdf_parser import process_resume
from typing import List
import asyncio
import spacy
import os


try:
    nlp = spacy.load("en_core_web_sm")
except:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


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

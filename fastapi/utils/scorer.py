from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_score(resume_text, job_desc):
    resume_embed = model.encode(resume_text, convert_to_tensor=True)
    jd_embed = model.encode(job_desc, convert_to_tensor=True)

    score = util.cos_sim(resume_embed, jd_embed).item()
    return round(score * 100, 2)

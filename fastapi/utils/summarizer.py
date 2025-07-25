def summarize(text):
    return text[:400] + "..."

# Test string
resume_text = """
Experienced software engineer with over 5 years of experience in Python, Django, and REST API development. 
Skilled in designing scalable backend systems, working with relational databases like PostgreSQL, 
and deploying applications on cloud platforms like AWS. Looking to leverage my technical and problem-solving 
skills in a challenging environment.
"""

# Function call
preview = summarize(resume_text)
print(preview)

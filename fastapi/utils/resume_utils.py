import re

def extract_details(text):
    # Email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email_match.group(0) if email_match else "Not found"

    # Phone (Pakistan-style +92 or 03..)
    phone_match = re.search(r'(\+92|0)?3\d{2}[-\s]?\d{7}', text)
    phone = phone_match.group(0) if phone_match else "Not found"

    # Name (simple guess: first line or line with 'Name')
    lines = text.strip().split('\n')
    name = lines[0].strip() if lines else "Not found"

    return {
        "name": name,
        "email": email,
        "phone": phone
    }


# python -m uvicorn main:app --reload --port 8000


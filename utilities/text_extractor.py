import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
def split_sections(text):
    text = text.lower()

    sections = {
        "skills": "",
        "experience": "",
        "projects": ""
    }

    if "skills" in text:
        sections["skills"] = text.split("skills")[1][:500]

    if "experience" in text:
        sections["experience"] = text.split("experience")[1][:700]

    if "projects" in text:
        sections["projects"] = text.split("projects")[1][:700]

    return sections

def extract_bullets(text):
    lines = text.split('\n')
    bullets = [line.strip() for line in lines if len(line.strip()) > 30]
    return bullets
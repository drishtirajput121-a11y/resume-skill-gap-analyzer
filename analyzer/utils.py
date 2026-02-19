from pypdf import PdfReader
import re


def extract_text_from_pdf(pdf_file):
    """
    Extract text safely from PDF.
    Handles None returns and formatting issues.
    """
    try:
        reader = PdfReader(pdf_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)

        return text.strip()

    except Exception as e:
        print("Error extracting PDF text:", e)
        return ""


def clean_text(text):
    """
    Clean text for better skill matching.
    Removes special characters and extra spaces.
    """
    text = text.lower()
    
    # Remove all non-alphanumeric characters
    text = re.sub(r'[^a-z0-9+#.]', '', text)

    return text


def analyze_resume_gap(resume_text, role_skills):
    """
    Compare resume text with role skills.
    Returns:
        matched_skills
        missing_skills
        score (percentage)
    """

    matched = []
    missing = []

    if not resume_text:
        return [], [skill.name for skill in role_skills], 0

    # Clean resume text once
    cleaned_resume = clean_text(resume_text)

    for skill in role_skills:
        skill_name = skill.name.strip()
        cleaned_skill = clean_text(skill_name)

        if cleaned_skill in cleaned_resume:
            matched.append(skill_name)
        else:
            missing.append(skill_name)

    total_skills = len(role_skills)
    score = (len(matched) / total_skills * 100) if total_skills > 0 else 0

    return matched, missing, round(score, 2)

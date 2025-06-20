import fitz
import requests
import os
from ml_agent.utils import is_url, clean_text

def parse_resume(link):
    try:
        if is_url(link):
            response = requests.get(link)
            path = "temp_resume.pdf"
            with open(path, "wb") as f:
                f.write(response.content)
        else:
            path = link

        text = ""
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()

        if os.path.exists("temp_resume.pdf"):
            os.remove("temp_resume.pdf")

        return clean_text(text)
    except Exception as e:
        print(f"❌ Failed to parse resume: {e}")
        return ""

import re
import pandas as pd

def is_url(link):
    return link.startswith("http://") or link.startswith("https://")

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.encode("ascii", errors="ignore").decode().strip()

def save_output(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

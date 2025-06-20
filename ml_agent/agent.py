import pandas as pd
from tqdm import tqdm
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ml_agent.resume_parser import parse_resume
from ml_agent.job_matcher import evaluate_resume
from ml_agent.utils import save_output
from sentence_transformers import SentenceTransformer

INPUT_CSV = "data/sample_resumes.csv"
JOB_FILE = "data/sample_job_description.txt"
OUTPUT_CSV = "sample_output.csv"

def parse_job_description(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            jd = f.read()
        model = SentenceTransformer("all-MiniLM-L6-v2")
        return model.encode(jd, convert_to_tensor=True)
    except Exception as e:
        print(f"❌ Error reading or embedding job description: {e}")
        return None

def main():
    job_embedding = parse_job_description(JOB_FILE)
    if job_embedding is None:
        print("❌ Failed to load job description.")
        return

    df = pd.read_csv(INPUT_CSV)
    results = []

    for _, row in tqdm(df.iterrows(), total=len(df)):
        name = row['name']
        link = row['resume_link']
        resume_text = parse_resume(link)
        score, reason = evaluate_resume(resume_text, job_embedding)
        results.append({"name": name, "resume_link": link, "score": score, "reasoning": reason})

    save_output(results, OUTPUT_CSV)
    print(f"✅ Done. Results saved to {OUTPUT_CSV}")

if __name__ == '__main__':
    main()

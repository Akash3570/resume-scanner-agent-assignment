from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_resume(resume_text, job_embedding):
    if not resume_text.strip():
        return 0.0, "Resume is empty or unreadable."
    try:
        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        similarity = util.cos_sim(job_embedding, resume_embedding).item()
        score = round(similarity * 10, 2)

        if score > 8:
            reason = "Strong match."
        elif score > 5:
            reason = "Partial match."
        else:
            reason = "Weak match."

        return score, reason
    except Exception as e:
        return 0.0, f"Evaluation failed: {e}"

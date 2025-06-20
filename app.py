import streamlit as st
import pandas as pd
from ml_agent.agent import main as evaluate_all

st.title("📄 Resume Evaluation Agent")

if st.button("Run Resume Evaluation"):
    with st.spinner("Evaluating resumes..."):
        evaluate_all()
    st.success("✅ Evaluation complete! Check `sample_output.csv` for results.")

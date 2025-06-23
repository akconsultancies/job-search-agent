import streamlit as st
from job_agent import get_jobs_from_remotive
from resume_utils import extract_text_from_pdf
from embedding_matcher import get_embedding, cosine_similarity

st.title("🔍 AI Resume-to-Job Matcher")

resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
query = st.text_input("Job Title", "Python Developer")

if st.button("Match Jobs") and resume_file:
    with st.spinner("Extracting resume..."):
        resume_text = extract_text_from_pdf(resume_file)
        resume_embedding = get_embedding(resume_text)

    with st.spinner("Searching and scoring jobs..."):
        jobs = get_jobs_from_remotive(query)
        for job in jobs:
            job_embedding = get_embedding(job["summary"])
            job["score"] = cosine_similarity(resume_embedding, job_embedding)

        ranked = sorted(jobs, key=lambda x: x["score"], reverse=True)

    st.success("Here are your top matches:")
    for job in ranked:
        st.subheader(f"{job['title']} at {job['company']}")
        st.write(job["summary"][:300] + "...")
        st.write(f"🔗 [Apply here]({job['link']})")
        st.write(f"🧠 Match Score: {round(job['score'], 2)}")

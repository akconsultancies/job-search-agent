import streamlit as st
from job_agent import get_jobs_from_indeed, match_score

st.title("🔍 AI Job Search Agent")

job_title = st.text_input("Job Title", "Python Developer")
location = st.text_input("Location", "London")
skills = st.text_input("Your Top Skills (comma-separated)", "Python, Django, API")

if st.button("Find Jobs"):
    skills_list = [s.strip() for s in skills.split(",")]
    jobs = get_jobs_from_indeed(job_title, location)
    for job in jobs:
        job["score"] = match_score(job["summary"], skills_list)
    ranked = sorted(jobs, key=lambda x: x["score"], reverse=True)
    
    for job in ranked:
        st.subheader(f"{job['title']} at {job['company']}")
        st.write(job['summary'])
        st.write(f"🔗 [Apply here]({job['link']})")
        st.write(f"⭐ Match Score: {round(job['score'], 2)}")

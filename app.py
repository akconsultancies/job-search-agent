import streamlit as st
from job_agent import get_jobs_from_indeed

st.title("AI Job Search Agent")

query = st.text_input("Job Title", "Python Developer")
location = st.text_input("Location", "London")

if st.button("Search"):
    try:
        jobs = get_jobs_from_indeed(query, location)
        if not jobs:
            st.warning("No jobs found.")
        for job in jobs:
            st.subheader(f"{job['title']} at {job['company']}")
            st.write(job['summary'])
            st.markdown(f"[Apply here]({job['link']})")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

import streamlit as st
from job_agent import get_jobs_from_remotive

st.title("AI Job Search Agent")

query = st.text_input("Job Title", "Python Developer")
location = st.text_input("Location", "London")

//search_url = f"https://remotive.com/api/remote-jobs?search={query}"
search_url = f"https://www.monster.com/jobs/search?q={query}&where=London%2C+UK"
st.write(f"📡 Query URL: {search_url}")

if st.button("Search"):
    jobs = get_jobs_from_remotive(query)
    if not jobs:
        st.warning("No jobs found.")
    for job in jobs:
        st.subheader(f"{job['title']} at {job['company']}")
        st.write(job['summary'])
        st.markdown(f"[Apply here]({job['link']})")

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def get_jobs_from_indeed(query, location, limit=5):
    jobs = []
    url = f"https://www.indeed.com/jobs?q={query}&l={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    postings = soup.find_all("a", {"class": "tapItem"}, limit=limit)

    for post in postings:
        title = post.find("h2").text.strip()
        company = post.find("span", {"class": "companyName"}).text.strip()
        summary = post.find("div", {"class": "job-snippet"}).text.strip()
        link = "https://www.indeed.com" + post.get("href")
        jobs.append({"title": title, "company": company, "summary": summary, "link": link})
    return jobs

def match_score(text, skills):
    return sum(SequenceMatcher(None, skill.lower(), text.lower()).ratio() for skill in skills)

if __name__ == "__main__":
    query = input("Job title (e.g., Python Developer): ")
    location = input("Location (e.g., London): ")
    skills = input("List your top 3 skills (comma-separated): ").split(",")

    jobs = get_jobs_from_indeed(query, location)
    for job in jobs:
        job["score"] = match_score(job["summary"], skills)

    ranked = sorted(jobs, key=lambda x: x["score"], reverse=True)

    for i, job in enumerate(ranked, start=1):
        print(f"\n{i}. {job['title']} at {job['company']} - Match Score: {round(job['score'], 2)}")
        print(job["summary"])
        print(f"Apply here: {job['link']}")

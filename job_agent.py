import requests
from bs4 import BeautifulSoup

def get_jobs_from_indeed(query, location, limit=5):
    jobs = []
    query = query.replace(" ", "+")
    url = f"https://www.indeed.com/jobs?q={query}&l={location}"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        postings = soup.find_all("a", {"class": "tapItem"}, limit=limit)
        
        for post in postings:
            try:
                title = post.find("h2").text.strip()
                company = post.find("span", {"class": "companyName"}).text.strip()
                summary = post.find("div", {"class": "job-snippet"}).text.strip()
                link = "https://www.indeed.com" + post.get("href")
                jobs.append({"title": title, "company": company, "summary": summary, "link": link})
            except Exception as e:
                continue  # Skip broken post
    except Exception as e:
        print("Error fetching jobs:", e)
    return jobs

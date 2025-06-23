import requests
from bs4 import BeautifulSoup

def get_jobs_from_indeed(query, location, limit=5):
    jobs = []
    query = query.replace(" ", "+")
    location = location.replace(" ", "+")
    
    url = f"https://www.indeed.com/jobs?q={query}&l={location}&fromage=last"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.select("a.tapItem")[:limit]
        
        for card in job_cards:
            title = card.select_one("h2.jobTitle span").get_text(strip=True)
            company = card.select_one("span.companyName").get_text(strip=True)
            summary_el = card.select_one("div.job-snippet")
            summary = summary_el.get_text(separator=" ", strip=True) if summary_el else ""
            link = "https://www.indeed.com" + card.get("href")
            jobs.append({
                "title": title,
                "company": company,
                "summary": summary,
                "link": link
            })

    except Exception as e:
        print(f"[Error] Scraping failed: {e}")
    
    return jobs

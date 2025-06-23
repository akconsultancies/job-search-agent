import requests

def get_jobs_from_remotive(query, limit=10):
    //url = f"https://remotive.com/api/remote-jobs?search={query}"
    url = f"https://www.monster.com/jobs/search?q={query}&where=London%2C+UK"
    jobs = []
    
    try:
        response = requests.get(url)
        data = response.json()
        for job in data.get("jobs", [])[:limit]:
            jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "summary": job["description"][:300],  # Trim to preview
                "link": job["url"]
            })
    except Exception as e:
        print(f"[Error] Remotive fetch failed: {e}")
    
    return jobs

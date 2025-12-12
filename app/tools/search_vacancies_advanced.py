# app/tools/search_vacancies_advanced.py
import requests
from typing import Optional

def search_vacancies_advanced(
    text: Optional[str] = None,
    area: Optional[int] = None,
    per_page: int = 10,
    page: int = 0,
    salary_from: Optional[int] = None,
    salary_to: Optional[int] = None,
    experience: Optional[str] = None,
    employment: Optional[str] = None,
    schedule: Optional[str] = None
) -> dict:
    params = {
        "per_page": per_page,
        "page": page
    }
    if text is not None:
        params["text"] = text
    if area is not None:
        params["area"] = area
    if salary_from is not None:
        params["salary_from"] = salary_from
    if salary_to is not None:
        params["salary_to"] = salary_to
    if experience is not None:
        params["experience"] = experience
    if employment is not None:
        params["employment"] = employment
    if schedule is not None:
        params["schedule"] = schedule

    headers = {
        "User-Agent": "Myapp2/1.0 (my-app@dsds.com)"
    }
    try:
        resp = requests.get("https://api.hh.ru/vacancies", params=params, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError:
        return {"error": "HTTP error", "status": resp.status_code, "body": resp.text}
    except requests.Timeout:
        return {"error": "Request timed out"}
    except Exception as e:
        return {"error": str(e)}

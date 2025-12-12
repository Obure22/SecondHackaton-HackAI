# app/tools/get_vacancy_details.py
import requests

def get_vacancy_details(vacancy_id: int) -> dict:
    """
    Get full information about a vacancy by its ID.
    """
    url = f"https://api.hh.ru/vacancies/{vacancy_id}"
    headers = {
        "User-Agent": "Myapp2/1.0 (my-app@dsds.com)"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError:
        return {"error": "HTTP error", "status": resp.status_code, "body": resp.text}
    except requests.Timeout:
        return {"error": "Request timed out"}
    except Exception as e:
        return {"error": str(e)}

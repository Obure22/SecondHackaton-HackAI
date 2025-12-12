# app/tools/search_vacancies.py
import requests

def search_vacancies(
    text: str,
    area: int | None = None,
    per_page: int = 10,
    page: int = 0
) -> dict:
    """
    Search vacancies on hh.ru (HeadHunter).

    Args:
        text: search keywords, e.g. "Python developer"
        area: region code (optional), e.g. "1" for Moscow
        per_page: number of results per page (default: 10)
        page: page number (default: 0)

    Returns:
        JSON dict as returned by https://api.hh.ru/vacancies
    """

    params = {
        "text": text,
        "per_page": per_page,
        "page": page
    }

    if area:
        params["area"] = area

    headers = {
        "User-Agent": "Myapp2/1.0 (my-app@dsds.com)"
    }

    try:
        resp = requests.get(
            "https://api.hh.ru/vacancies",
            params=params,
            headers=headers,
            timeout=15
        )
        resp.raise_for_status()
        return resp.json()

    except requests.Timeout:
        return {"error": "Request timed out"}

    except requests.HTTPError as e:
        return {
            "error": "HTTP error",
            "status": resp.status_code,
            "body": resp.text
        }

    except Exception as e:
        return {"error": str(e)}

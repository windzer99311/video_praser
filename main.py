from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.post("/")
def get_stream(data: dict):
    url = data.get("url")
    if not url:
        return {"error": "Missing URL"}

    api = "https://api.vidssave.com/api/contentsite_api/media/parse"

    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://vidssave.com",
        "referer": "https://vidssave.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    payload = {
        "auth": os.getenv("VIDSSAVE_AUTH", "20250901majwlqo"),
        "domain": "api-ak.vidssave.com",
        "origin": "source",
        "link": url
    }

    try:
        r = requests.post(api, headers=headers, data=payload, timeout=15)
        return {
            "status_code": r.status_code,
            "headers": dict(r.headers),
            "body": r.json()  # returns as JSON
        }
    except Exception as e:
        return {"error": str(e)}

import json
import requests
import os

def main(context):
    try:
        body = json.loads(context.req.body or "{}")
        url = body.get("url")

        if not url:
            return context.res.json(
                {"error": "url is required"},
                status=400
            )

        api = "https://api.vidssave.com/api/contentsite_api/media/parse"

        headers = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://vidssave.com",
            "referer": "https://vidssave.com/",
            "user-agent": "Mozilla/5.0"
        }

        payload = {
            "auth": os.getenv("VIDSSAVE_AUTH", "20250901majwlqo"),
            "domain": "api-ak.vidssave.com",
            "origin": "source",
            "link": url
        }

        r = requests.post(api, headers=headers, data=payload, timeout=15)

        return context.res.json({
            "status_code": r.status_code,
            "body": r.text
        })

    except Exception as e:
        return context.res.json(
            {"error": str(e)},
            status=500
        )

import requests

def main(context):
    try:
        # Body is already parsed by Appwrite
        data = context.req.body or {}
        url = data.get("url")

        if not url:
            context.res.status(400)
            return context.res.json({"error": "url is required"})

        api = "https://api.vidssave.com/api/contentsite_api/media/parse"

        headers = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://vidssave.com",
            "referer": "https://vidssave.com/",
            "user-agent": "Mozilla/5.0"
        }

        payload = {
            "auth": "20250901majwlqo",
            "domain": "api-ak.vidssave.com",
            "origin": "source",
            "link": url
        }

        r = requests.post(api, headers=headers, data=payload, timeout=15)

        context.res.status(r.status_code)
        return context.res.json({
            "body": r.text
        })

    except Exception as e:
        context.res.status(500)
        return context.res.json({
            "error": str(e)
        })

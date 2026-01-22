import requests

def main(context):
    # This checks for 'link' OR 'video_url'
    link="https://youtu.be/z3UHfi9vpbc?si=yk6j3HPOU61qhttN"
    
    if not link:
        # This is the 400 error you just saw
        return context.res.json({"error": "No link provided"}, 400)

    context.log(f"Processing link: {link}")
    api="https://api.vidssave.com/api/contentsite_api/media/parse"
    headers = {
        "origin": "https://vidssave.com",
        "referer": "https://vidssave.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"
    }
    data={
        "auth": "20250901majwlqo",
        "domain": "api-ak.vidssave.com",
        "origin": "source",
        "referer": "https://vidssave.com/",
        "link": f"{link}"
    }

    response = requests.post(api, headers=headers,data=data,timeout=5)
    audio_stream=None
    size=None
    print("status code:",response.status_code)
    print("response:",response.json())
    if response.status_code==200:
        a=response.json()
        return a
    else:
        b="Failed"
        return b

import requests

def main(context):
    # This checks for 'link' OR 'video_url'
    link="https://youtu.be/z3UHfi9vpbc?si=yk6j3HPOU61qhttN"
    
    if not link:
        # This is the 400 error you just saw
        return context.res.json({"error": "No link provided"}, 400)

    context.log(f"Processing link: {link}")

    try:
        api = "https://api.vidssave.com/api/contentsite_api/media/parse"
        headers = {
            "origin": "https://vidssave.com",
            "referer": "https://vidssave.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"
        }
        data = {
            "auth": "20250901majwlqo",
            "domain": "api-ak.vidssave.com",
            "origin": "source",
            "referer": "https://vidssave.com/",
            "link": link
        }

        # Make the request to the external API
        response = requests.post(api, headers=headers, data=data, timeout=10)
        response_data = response.json()
        
        # Extract the data
        a = response_data.get("data", {})
        resources = a.get("resources", [])
        
        audio_stream = None

        for items in resources:
            if items.get("quality") == "48KBPS":
                audio_stream = items.get("download_url")
                break

        if audio_stream:
            return context.res.json({
                "success": True,
                "stream": audio_stream
            })
        else:
            return context.res.json({
                "success": False, 
                "message": "Audio stream not found",
                "raw_data": a # Useful for debugging in the logs
            })

    except Exception as e:
        context.error(f"Error occurred: {str(e)}")
        return context.res.json({"error": "Internal server error", "details": str(e)}, 500)

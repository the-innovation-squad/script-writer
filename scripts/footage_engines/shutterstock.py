import requests
from config import config

def search_footage(prompt, footage_options, used_footage):
    aspect_ratio = footage_options["engine_settings"].get("aspect_ratio", "16_9")
    per_page = 10

    shutterstock_api_key = config["SHUTTERSTOCK_API_KEY"]
    headers = {
        "Authorization": f"Bearer {shutterstock_api_key}"
    }
    params = {
        "query": prompt,
        "per_page": per_page,
        "aspect_ratio": aspect_ratio,
        "sort": "relevance" # popular might be useful too
    }
    url = "https://api.shutterstock.com/v2/videos/search"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        videos = results.get("data")
        if videos:
            for video in videos:
                clip = video.get("assets").get("preview_mp4").get("url")
                if clip not in used_footage:
                    used_footage.append(clip)
                    return clip
        return None
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        raise Exception("Pexels API search failed: " + response.content)

def search(prompts, footage_options, used_footage):
    for prompt in prompts:
        result = search_footage(prompt, footage_options, used_footage)
        if result is not None:
            return result
    raise Exception("No results found for prompts: " + ", ".join(prompts))
import requests
from config import Config
cfg = Config()

def search_footage(prompt, footage_options, used_footage):
    orientation = footage_options["engine_settings"].get("orientation", "landscape")
    print(orientation)
    per_page = 10

    headers = {
        "Content-Type": "application/json",
        "Authorization": cfg.pexels_api_key
    }
    url=f"https://api.pexels.com/videos/search?query={prompt}&per_page={per_page}&orientation={orientation}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        videos = results.get("videos")
        if videos:
            for video in videos:
                clip = video.get("video_files")[0].get("link")
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
    raise Exception("No results found for prompts: " + prompts.join(", "))
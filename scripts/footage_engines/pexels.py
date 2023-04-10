import requests
import random
from config import Config
cfg = Config()

def search_footage(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": cfg.pexels_api_key
    }
    url=f"https://api.pexels.com/videos/search?query={prompt}&per_page=3"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        videos = results.get("videos")
        if videos:
            random_clip = random.choice(videos)
            return random_clip.get("video_files")[0].get("link")
        return None
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        raise Exception("Pexels API search failed: " + response.content)

def search(prompts):
    for prompt in prompts:
        result = search_footage(prompt)
        if result is not None:
            return result
    raise Exception("No results found for prompts: " + prompts.join(", "))
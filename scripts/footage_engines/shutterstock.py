import requests
import random
from config import Config
cfg = Config()

def search_footage(prompt):
    headers = {
        "Authorization": f"Bearer {cfg.shutterstock_api_key}"
    }
    params = {
        "query": prompt,
        "per_page": "3",
        "sort": "relevance" # popular might be useful too
    }
    url = "https://api.shutterstock.com/v2/videos/search"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        data = results.get("data")
        if data:
            random_clip = random.choice(data)
            return random_clip.get("assets").get("preview_mp4").get("url")
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
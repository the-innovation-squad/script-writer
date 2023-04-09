import requests
from config import Config
cfg = Config()

def search_footage(keywords):
    headers = {
        "Content-Type": "application/json",
        "Authorization": cfg.pexels_api_key
    }
    url=f"https://api.pexels.com/videos/search?query={keywords}&per_page=1"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        return results["videos"][0]["video_files"][0]["link"]
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        raise Exception("Pexels API search failed: " + response.content)

def add_footage(keyword_script):
    for item in keyword_script["timeline"]:
        clip = search_footage(item["tags"])
        item["clip"] = clip
        del item["tags"]
    return keyword_script
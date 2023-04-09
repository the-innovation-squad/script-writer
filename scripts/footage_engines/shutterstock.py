import requests
from config import Config
cfg = Config()

def search_footage(tag):
    headers = {
        "Authorization": f"Bearer {cfg.shutterstock_api_key}"
    }
    params = {
        "query": tag,
        "per_page": "1",
        "sort": "relevance" # popular might be useful too
    }
    url = "https://api.shutterstock.com/v2/videos/search"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        data = results.get("data")
        if data:
            return data[0].get("assets").get("preview_mp4").get("url")
        return None
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
        raise Exception("Pexels API search failed: " + response.content)

def search(tags):
    tags_array = tags.split(",")
    for tag in tags_array:
        result = search_footage(tag.strip())
        if result is not None:
            return result
    raise Exception("No results found for tags: " + str(tags))
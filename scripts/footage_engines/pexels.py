import requests
from config import Config
cfg = Config()

def search_footage(prompt, footage_options, used_footage):
    orientation = footage_options["engine_settings"].get("orientation", "landscape")
    per_page = 10

    pexels_api_key = cfg.get_or_throw("pexels_api_key")

    headers = {
        "Content-Type": "application/json",
        "Authorization": pexels_api_key
    }
    url=f"https://api.pexels.com/videos/search?query=\"{prompt}\"&per_page={per_page}&orientation={orientation}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        videos = results.get("videos")
        if videos:
            for video in videos:
                clips = video.get("video_files")
                hd_clips = [clip for clip in clips if clip.get("quality") == "hd"]
                clip = hd_clips[0].get("link")
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
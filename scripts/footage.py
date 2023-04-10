from footage_engines.pexels import search as pexels_search
from footage_engines.shutterstock import search as shutterstock_search

def add_footage(keyword_script, footage_options):
    engine = footage_options["engine"]

    for item in keyword_script["timeline"]:
        prompts = item["image_prompts"]

        if engine == "pexels":
            clip = pexels_search(prompts)
        elif engine == "shutterstock":
            clip = shutterstock_search(prompts)
        else:
            raise Exception("Invalid footage engine: " + engine)

        item["clip"] = clip
        del item["image_prompts"]
    return keyword_script
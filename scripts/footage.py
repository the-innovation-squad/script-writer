from footage_engines.pexels import search as pexels_search
from footage_engines.shutterstock import search as shutterstock_search

def add_footage(keyword_script, footage_options):
    engine = footage_options["engine"]

    for item in keyword_script["timeline"]:
        tags = item["tags"]

        if engine == "pexels":
            clip = pexels_search(tags)
        elif engine == "shutterstock":
            clip = shutterstock_search(tags)
        else:
            raise Exception("Invalid footage engine: " + engine)

        item["clip"] = clip
        del item["tags"]
    return keyword_script
from footage_engines.pexels import search_footage as pexels_search

def add_footage(keyword_script, footage_options):
    engine = footage_options["engine"]

    for item in keyword_script["timeline"]:

        if engine == "pexels":
            clip = pexels_search(item["tags"])
        else:
            raise Exception("Invalid footage engine: " + engine)

        item["clip"] = clip
        del item["tags"]
    return keyword_script
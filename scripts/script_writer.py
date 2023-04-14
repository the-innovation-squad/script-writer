import yaml
from config import config
from content_writer import generate_keyword_script
from footage import add_footage

def write_script(prompt, output_dir):
    """Generate a video script containing text and corresponding footage"""
    with open("input/settings.yml", "r") as file:
        input_settings = yaml.safe_load(file)
    print("> Input Settings:", input_settings)

    script_options = {
            "style": input_settings.get("script_style", config["script"]["style"]),
            "max_content_length": input_settings.get("max_content_length", config["script"]["max_content_length"]),
            "max_timeline_entries": input_settings.get("max_timeline_entries", config["script"]["max_timeline_entries"])
    }
    footage_options = {
        "engine": input_settings.get("footage_engine", config["footage"]["engine"]),
        "engine_settings": input_settings.get("footage_engine_settings", {})
    }
    print("> Script Options:", script_options)
    print("> Footage Options:", footage_options)

    print("> Generating keyword script...")
    keyword_script = generate_keyword_script(prompt, script_options)
    with open("output/tag_script.yml", "w") as outfile:
        yaml.dump(keyword_script, outfile, default_flow_style=False)

    print("> Adding footage...")
    script_with_footage = add_footage(keyword_script, footage_options)

    print("> Writing output...")
    with open(f"{output_dir}/output.yml", "w") as outfile:
        yaml.dump(script_with_footage, outfile, default_flow_style=False)
    print("> Done.")



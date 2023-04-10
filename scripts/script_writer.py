import yaml
from content_writer import generate_keyword_script
from footage import add_footage

def write_script():
        with open("input/text.txt", "r") as file:
            input_text = file.read()

        with open("input/settings.yml", "r") as file:
            input_settings = yaml.safe_load(file)

        script_options = {
             "style": input_settings.get("script_style", "informative"),
        }
        footage_options = {
             "engine": input_settings.get("footage_engine", "pexels")
        }

        keyword_script = generate_keyword_script(input_text, script_options)
        with open("output/tag_script.yml", "w") as outfile:
            yaml.dump(keyword_script, outfile, default_flow_style=False)

        script_with_footage = add_footage(keyword_script, footage_options)
        with open("output/output.yml", "w") as outfile:
            yaml.dump(script_with_footage, outfile, default_flow_style=False)



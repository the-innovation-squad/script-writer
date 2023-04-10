import openai
import yaml
from config import Config
cfg = Config()

openai.api_key = cfg.openai_api_key

def generate_keyword_script(input_text):
    if cfg.debug:
        with open("lib/tags_script.yml", "r") as file:
            tags_script = yaml.safe_load(file)
        return tags_script

    with open("lib/instructions.txt", "r") as file:
        instructions = file.read()

    # to prevent the response from using too many tokens and cutting short
    intended_video_length_seconds = 30
    maximum_timeline_entries = 6
    max_content_characters = 300

    style="informative"

    # instructions += f"The video should be {intended_video_length_seconds} seconds long.\n"
    # instructions += f"The video should have a maximum of {maximum_timeline_entries} entries.\n"
    # instructions += f"Each content entry should be a maximum of {max_content_characters} characters.\n"
    instructions += f"The video should be {style}.\n"
    instructions += "\n[START INPUT TEXT]\n"
    prompt = instructions + input_text
    prompt += "\n[END INPUT TEXT]"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1200,
        n=1,
        stop=None,
        temperature=0.7,
    )

    script_yaml_string = response.choices[0].text.strip()
    with open("output/openai_response.txt", "w") as file:
        file.write(script_yaml_string)

    script_yaml = yaml.safe_load(script_yaml_string)
    return script_yaml

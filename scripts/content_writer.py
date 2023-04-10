import openai
import yaml
from config import Config
cfg = Config()

openai.api_key = cfg.openai_api_key

def generate_keyword_script(input_text, script_options):
    if cfg.debug:
        with open("lib/tags_script.yml", "r") as file:
            tags_script = yaml.safe_load(file)
        return tags_script

    with open("lib/instructions.txt", "r") as file:
        instructions = file.read()

    style = script_options["style"]
    instructions += f"\nThe video should be {style}.\n"
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

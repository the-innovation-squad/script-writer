import openai
import yaml
from config import Config
cfg = Config()

openai.api_key = cfg.openai_api_key

def generate_keyword_script(input_text):
    if cfg.debug:
        with open("lib/sample_keyword_script.yml", "r") as file:
            sample_keyword_script = yaml.safe_load(file)
        return sample_keyword_script

    with open("lib/instructions.txt", "r") as file:
        instructions = file.read()

    video_length_seconds = 30
    instructions += f"The video should be {video_length_seconds} seconds long.\n"
    instructions += "START INPUT TEXT:\n"

    prompt = instructions + input_text

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    script_yaml_string = response.choices[0].text.strip()
    script_yaml = yaml.safe_load(script_yaml_string)
    return script_yaml

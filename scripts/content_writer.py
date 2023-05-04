import openai
import yaml
from jinja2 import Template
from config import config

openai.api_key = config["OPENAI_API_KEY"]

def generate_keyword_script(input_text, script_options):
    if config["debug"]:
        print("> DEBUG enabled, using pre-generated script...")
        with open("lib/script_no_footage.yml", "r") as file:
            script_no_footage = yaml.safe_load(file)
        return script_no_footage

    with open("lib/prompt_template.txt", "r") as file:
        prompt_template_string = file.read()
    prompt_template = Template(prompt_template_string)
    system_prompt = prompt_template.render(script_options)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": input_text}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    script_yaml_string = response.choices[0].message['content'].strip()
    with open("output/openai_response.txt", "w") as file:
        file.write(script_yaml_string)

    script_yaml = yaml.safe_load(script_yaml_string)
    return script_yaml
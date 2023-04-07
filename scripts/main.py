import openai
import yaml
from config import Config
cfg = Config()

openai.api_key = cfg.openai_api_key

def generate_chat_response(user_prompt):
    with open("input/prompt.txt", "r") as file:
        system_prompt = file.read()

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Create a 20 second video script based on the following description:\n\n{user_prompt}\n\n{system_prompt}",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def create_yml(prompt):
    yml_content = generate_chat_response(prompt)
    yml_data = yaml.safe_load(yml_content)

    with open("output/output.yml", "w") as outfile:
        yaml.dump(yml_data, outfile, default_flow_style=False)

if __name__ == "__main__":
    user_prompt = input("Please enter a plain English prompt: ")
    create_yml(user_prompt)
    print("YAML file created: output/output.yml")

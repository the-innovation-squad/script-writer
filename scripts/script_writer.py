import yaml
from open_ai import generate_keyword_script
from footage import add_footage

def write_script():
        with open("input/text.txt", "r") as file:
            input_text = file.read()

        keyword_script = generate_keyword_script(input_text)
        script_with_footage = add_footage(keyword_script)

        with open("output/output.yml", "w") as outfile:
            yaml.dump(script_with_footage, outfile, default_flow_style=False)



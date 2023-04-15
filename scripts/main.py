from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

import argparse
from config import config
import os
import shutil
import yaml
from script_writer import write_script

def clear_ouput_directory():
    output_dir = "output"
    file_to_keep = ".gitkeep"
    for item in os.listdir(output_dir):
        item_path = os.path.join(output_dir, item)
        if item != file_to_keep:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

def configure_args():
    parser = argparse.ArgumentParser(description="Generate a video from a script.")

    # positional arguments are based on the order they are defined here
    parser.add_argument("-p", "--prompt", help="The prompt to generate a script from")
    parser.add_argument("-o", "--output", help="The output directory to write the script to")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    return parser.parse_args()

if __name__ == "__main__":
    clear_ouput_directory()

    args = configure_args()
    config = {}
    config["debug"] = args.debug
    config["output_dir"] = args.output if args.output else "output"

    if(args.prompt):
        prompt = args.prompt
    else:
        with open("input/text.txt", "r") as file:
            prompt = yaml.safe_load(file)

    write_script(prompt)
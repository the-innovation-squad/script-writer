import argparse
import os
import shutil
from script_writer import write_script
from config import Config
cfg = Config()

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
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    cfg.update_from_args(args)
    cfg.log_args()


if __name__ == "__main__":
    configure_args()
    clear_ouput_directory()
    write_script()
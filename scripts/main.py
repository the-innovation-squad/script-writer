import os
import shutil
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


if __name__ == "__main__":
    clear_ouput_directory()
    write_script()
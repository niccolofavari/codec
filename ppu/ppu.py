import os
import sys
import argparse

DELIMITER = "#======#"

def pack_project(root_dir):
    """
    Packs a Python project into a single concatenated file.

    :param root_dir: The root directory of the Python project.
    :return: A string containing the concatenated project files.
    """
    concatenated_code = ""
    for folder, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(folder, file)
                with open(file_path, "r") as f:
                    file_content = f.read().strip()
                relative_path = os.path.join(root_dir, os.path.relpath(file_path, root_dir))
                delimiter_with_path = f"{DELIMITER} {relative_path} {DELIMITER}"
                concatenated_code += f"{delimiter_with_path}\n{file_content}\n"
    return concatenated_code

def unpack_project(input_file_name, project_root):
    """
    Unpacks a Python project from a concatenated file.

    :param input_file_name: The name of the input file containing the concatenated project.
    :param project_root: The root directory for the reconstructed project.
    """
    with open(input_file_name, "r") as input_file:
        content = input_file.read()

    file_blocks = content.split(DELIMITER)[1:]

    for i in range(0, len(file_blocks), 2):
        file_path = file_blocks[i].strip()
        file_content = file_blocks[i+1].strip()

        dir_path = os.path.dirname(file_path)
        if not dir_path:
            dir_path = "."

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "w") as output_file:
            output_file.write(file_content)

def main():
    """
    Main function that handles command-line arguments and executes the appropriate command.
    """
    parser = argparse.ArgumentParser(description="Pack and unpack Python projects")
    parser.add_argument("command", choices=["pack", "unpack"], help="Command to execute: pack or unpack")
    parser.add_argument("project_folder", help="Path to the project folder")

    args = parser.parse_args()

    command = args.command
    project_folder = args.project_folder

    if command == "pack":
        concatenated_source_code = pack_project(project_folder)
        output_file_name = f"{project_folder}.txt"

        with open(output_file_name, "w") as output_file:
            output_file.write(concatenated_source_code)

    elif command == "unpack":
        input_file_name = f"{project_folder}.txt"
        unpack_project(input_file_name, project_folder)

    else:
        print("Invalid command. Use 'pack' or 'unpack'.")
        sys.exit(1)
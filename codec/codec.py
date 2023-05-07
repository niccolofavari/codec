import os
import sys

DELIMITER = "#======#"

def concatenate_files(root_dir):
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

def reconstruct_project(input_file_name, project_root):
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
    if len(sys.argv) != 3:
        print("Usage: codec <command> <project_folder>")
        sys.exit(1)

    command = sys.argv[1]
    project_folder = sys.argv[2]

    if command == "concat":
        concatenated_source_code = concatenate_files(project_folder)
        output_file_name = f"{project_folder}.txt"

        with open(output_file_name, "w") as output_file:
            output_file.write(concatenated_source_code)

    elif command == "decat":
        input_file_name = f"{project_folder}.txt"
        reconstruct_project(input_file_name, project_folder)

    else:
        print("Invalid command. Use 'concat' or 'decat'.")
        sys.exit(1)
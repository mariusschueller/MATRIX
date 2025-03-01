import os
import json

def main():
    if os.path.exists("dir_paths.json"):
        return print("dir_paths.json exists!")

    input_dir_path = input("Enter the path to input stl file directory: ")

    output_dir_path = input("Enter the path to output stl file directory: ")

    if os.path.exists(input_dir_path) and os.path.exists(output_dir_path):
        dir_paths = {
            "input_dir_path": input_dir_path,
            "output_dir_path": output_dir_path
        }
        json_object = json.dumps(dir_paths, indent=4)
        with open("dir_paths.json", "w") as outfile:
            outfile.write(json_object)
        print("Directory paths saved to dir_paths.json")

    else:
        print("Invalid directory path")

def get_dir():
    current_directory = os.getcwd()
    current_directory = current_directory.replace("api", "")
    print(current_directory)
    return current_directory

if __name__ == "__main__":
    get_dir()
    main()
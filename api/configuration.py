import os
import json
import sys

def main():
    if os.path.exists("dir_paths.json"):
        print("dir_paths.json exists!")
        return
    
    # Expecting two arguments: input_dir_path and output_dir_path, use environment variables if not provided
    if len(sys.argv) == 0:
        input_dir_path = os.getenv("STL_INPUT_DIR", "/app/stl_input")
        output_dir_path = os.getenv("GCODE_OUTPUT_DIR", "/app/gcode_output")
    
    elif len(sys.argv) == 3:
        input_dir_path = sys.argv[1]
        output_dir_path = sys.argv[2]

    else:
        print("Usage: python3 configuration.py <input_dir_path> <output_dir_path>")
        sys.exit(1)
    

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
    main()
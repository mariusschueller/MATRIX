from flask import Flask
import subprocess
import os
import sizing


app = Flask(__name__)

def preCheck(filename, file_path):
    # check if it's an stl file
    if not checkSTL(filename):
        print("Invalid file format", 400)
        return False

    # check if the file_path is valid
    
    if not os.path.exists(file_path):
        print(f"File {filename} does not exist", 404)
        return False
    
    return True

# Check if the file ends with .stl
def checkSTL(file):
    if file.endswith(".stl"):
        return True
    return False

# Reorient the part
def tweak(file_path):
    # prepare the command to be executed
    sub = [
    "python3",
    "/home/marius/Documents/MATRIX/Tweaker-3/Tweaker.py",
    "-i",
    file_path,
    "-vb"
    ]

    print("Executing:", sub)

    # call the Tweaker.py script
    result = subprocess.run(
        sub,
        capture_output=True,
        text=True
    )
    print("Orientated part")

    # return the new file path
    return file_path.replace(".stl", "_tweaked.stl")

# Call to get the size of the model
@app.route('/size/<filename>')
def size(filename):
    file_path = f"/home/marius/Documents/MATRIX/test_files/{filename}"
    
    if not preCheck(filename, file_path):
        return "Failed precheck"

    # Pass the full file_path to tweak and update file_path with its return value.
    file_path = tweak(file_path)

    print(file_path)

    # Now get the size from sizing.py
    result = sizing.getSize(file_path)

    return result


# Just a very basic slicing call
@app.route('/file/<filename>')
def file(filename):
    file_path = f"/home/marius/Documents/MATRIX/test_files/{filename}"
    
    if not preCheck(filename, file_path):
        return "Failed precheck"
    
    result = subprocess.run(
        [
            "/home/marius/Documents/MATRIX/superslicer/superslicer",
            "-g",
            f"/home/marius/Documents/MATRIX/test_files/{filename}"
        ],
        capture_output=True,
        text=True
    )
    output = result.stdout.split("\n")
    error = result.stderr
    return output
    

# This call orients the part and allows for parameters
@app.route('/fileOptions/<file>/<options>')
def fileAndOption(file, options):
    file_path = f"/home/marius/Documents/MATRIX/test_files/{file}"
    
    if not preCheck(file, file_path):
        return "Failed precheck"

    file_path = tweak(file_path)

    # prepare superslicer command
    options_list = options.split()  
    print(options_list)
    sub = [
        "/home/marius/Documents/MATRIX/superslicer/superslicer", 
        "-g",
        file_path
    ] + options_list

    print("Executing:", sub)
    
    result = subprocess.run(
        sub,
        capture_output=True,
        text=True
    )
    
    output = result.stdout.split("\n")
    error = result.stderr
    return error

if __name__ == '__main__':
    app.run(debug=True)
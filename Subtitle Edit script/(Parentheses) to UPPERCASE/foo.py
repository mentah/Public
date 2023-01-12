"""
To write to a new file:
$   python foo.py <subtitle-file> <new-file>
To overwrite the same file:
$   python foo.py <subtitle-file>
"""

import re
import sys

def to_upper_parentheses(string):
    return re.sub(r'\(([^)]+)\)', lambda x: x.group(1).upper(), string)

if __name__ == "__main__":
    # Check if the file name is provided
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please provide the source file name./ Invalid argument(s)")
        exit()
    # Open the source file for reading
    with open(sys.argv[1], "r") as f:
        # Read the entire file into a string
        contents = f.read()
        # Convert the contents to uppercase
        contents = to_upper_parentheses(contents)
    # Check if the destination file name is provided
    if len(sys.argv) == 3:
        # Open the destination file for writing
        with open(sys.argv[2], "w") as f:
            # Write the modified contents to the new file
            f.write(contents)
        print(f"File {sys.argv[1]} has been written to {sys.argv[2]}.")
    if len(sys.argv) == 2:
        # Open the source file for writing
        with open(sys.argv[1], "w") as f:
            # Write the modified contents back to the file
            f.write(contents)
        print(f"File {sys.argv[1]} has been modified.")

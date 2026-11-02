"""
Reading from files allows us to import and process existing data
"""

file_path = "colors.txt"
try:
    with open(file_path, "r") as file:
        content = file.read() #reads in the entire file
    print(content)
except FileNotFoundError:
    print(f"{file_path} does not exist")
except PermissionError:
    print(f"You don't have permission to access {file_path}")

# Read in the file one line at a time:
colors = []
try:
    with open(file_path, "r") as file:
        for line in file:
            colors.append(line.strip())
        print(colors)
except FileNotFoundError:
    print(f"{file_path} does not exist")
except PermissionError:
    print(f"You don't have permission to access {file_path}")
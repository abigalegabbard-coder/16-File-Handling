"""
File detection means checking if a file or folder exists in a given location 
before your program tries to do anything with it.

In Python, to work with files, you need the os module. The os module is for interaction with the Operating System
"""

import os

file_path = "demo_01_test.txt" #notes: this is a RELATIVE path
#relative means, based on from the present working directory (where the program is running)

#see if our file exists:
if os.path.exists(file_path):
    print(f" The file path {file_path} exists.")
else:
    print(f" The file path {file_path} DOES NOT exist.")


file_path2 = "text_files/demo_01_test2.txt" #relative path
if os.path.exists(file_path2):
    print(f" The file path {file_path} exists.")
else:
    print(f" The file path {file_path} DOES NOT exist.")

#\n

# Bad - file_path3 = "C:\Users\CMP_abgabbard\OneDrive - Erie County Technical School\Desktop\Level 1 26-27\Notes\16 File Handling\text_files\demo_01_test2.txt"
# file_path3 = "C:\Users\CMP_abgabbard\OneDrive - Erie County Technical School\Desktop\Level 1 26-27\Notes\16 File Handling\text_files\demo_01_test2.txt"
# Works - forward slashes = file_path3 = "C:/Users/CMP_abgabbard/OneDrive - Erie County Technical School/Desktop/Level 1 26-27/Notes/16 File Handling/text_files/demo_01_test2.txt"
# Works - escape the backslash = file_path3 = "C:\\Users\\CMP_abgabbard\\OneDrive - Erie County Technical School\\Desktop\\Level 1 26-27\\Notes\\16 File Handling\\text_files\\demo_01_test2.txt"
# Works - raw strings. Place and "r" before the string = 
# file_path3 = r"C:\Users\CMP_abgabbard\OneDrive - Erie County Technical School\Desktop\Level 1 26-27\Notes\16 File Handling\text_files\demo_01_test2.txt"
file_path3 = "C:/Users/CMP_abgabbard/OneDrive - Erie County Technical School/Desktop/Level 1 26-27/Notes/16 File Handling/text_files/demo_01_test2.txt"
if os.path.exists(file_path3):
    print(f" The file path {file_path} exists.")
else:
    print(f" The file path {file_path} DOES NOT exist.")

file_path4 = "C:/Users/CMP_abgabbard/OneDrive - Erie County Technical School/Desktop/Level 1 26-27/Notes/16 File Handling/text_files/demo_01_test2.txt"
# Dectecting if it's a file or a folder:
if os.path.exists(file_path4):
    if os.path.isfile(file_path4):
        print(f" The location {file_path4} exists and it is a FILE")
    elif os.path.isdir(file_path4):
        print(f"The location {file_path4} exists and is a DIRECTORY")
else:
    print(f" The file path {file_path4} DOES NOT exist.")

# Detecting is a path is valid
# Determining if it is a file or a directory
# Relative vs absolute paths

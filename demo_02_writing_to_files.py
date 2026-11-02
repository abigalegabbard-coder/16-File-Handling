"""
Why write to files?
- hold information such as game scores, user settings, notes or logs, large datasets

3 common types of data files
- plain text(.txt)
- comma seperated values (.csv)
- json (javascript object notation) (.json)
"""

# Writing to a plain text file:
text_data = "um....gibberish"
file_path = "text_files/demo_02_file01.txt" #this is where we will wave our data
# The preferred and safests way to handle files is with the WITH statement
# WITH will open the file and automatically close if (free the resources) even if an error occurs
# Open is the function to open a file. "W" opens it in write mode
# Note: with "w" if the file already exists, it will be overwritten
with open(file_path, "w") as file:
    file.write(text_data)

#file_path2 = "../annoying file.txt"
## ../ means go UP one directory
#with open(file_path2, "w") as file:
#    file.write("I am a super annoying file. Can you find me?")
#
## Use with caution:
## delete a file:
#import os
#if os.path.exists(file_path2):
#    os.remove(file_path2)

# But what if we don't want to overwrite the file every time?!
# Instead of using "w", we will use: "a", which stands for "append"
with open(file_path, "a") as file:
    file.write("\nThe result of inflation on duck tokens has led to more trade and intrest in baby ducks.")

# There is an "x" (exculusive creation) flag you can use, which will throw an error if the file already exists
# So if you want to create a file, but not overwrite one:
try:
    with open(file_path, "x") as file:
        file.write("I'm only here because the file did not exist")
    print("File created succussully")
except FileExistsError:
    print("That file already exists. No data written")

colors = ["Blue", "Maroon", "Purple", "Red", "Green"]
with open("colors.txt", "w") as file:
    for color in colors:
        file. write(color + "\n")

with open(colors.txt, "w") as file:
    file.write(",".join(colors))
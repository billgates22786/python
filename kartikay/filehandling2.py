#Opening and Closing Files
file = open("example.txt", "r")  # Opens file in read mode
file.close()  # Closes the file

#Write
file = open("example.txt", "w")  # Opens the file in write mode

#REading lines
file = open("example.txt", "r")
content = file.read()  # Reads entire content of the file
file.close()

# Reading line by line
file = open("example.txt", "r")
line = file.readline()  # Reads a single line
file.close()

#Writing to files 
file = open("example.txt", "w")
file.write("Hello, World!")  # Writes to the file
file.close()

# Writing multiple lines
lines = ["First line\n", "Second line\n"]
file = open("example.txt", "w")
file.writelines(lines)  # Writes multiple lines
file.close()

#Appending to files 
file = open("example.txt", "a")
file.write("This will be appended.")  # Appends to the file
file.close()

#File Positioning 
file = open("example.txt", "r")
file.seek(10)  # Moves the pointer to the 10th byte
position = file.tell()  # Gets the current position of the pointer
file.close()

#File Deletion and Renaming 
import os
os.remove("example.txt")  # Deletes the file
os.rename("old_name.txt", "new_name.txt")  # Renames the file


#Checking if file exists
import os
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")

#With statement for file handling
with open("example.txt", "r") as file:
    content = file.read()  # No need to manually close the file

#Working with binary files
with open("image.jpg", "rb") as binary_file:
    data = binary_file.read()  # Reading binary data

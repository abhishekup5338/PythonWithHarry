
# Create an OS and list all the directories/folder which is currently in that path
import os

# Specify the directory path
directory_path = '/'

# Get the list of all files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of directory:", directory_path)
for item in contents:
    print(item)

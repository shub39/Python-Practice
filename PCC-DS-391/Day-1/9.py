# Write all content of a given file into a new file by skipping line number 5
# Create a test.txt file and add the below content to it.

newFileList = []

with open("test.txt", "r") as file:
    for line in file:
        if line != "line5\n":
            newFileList.append(line)

with open("new_file.txt", "w") as file:
    for line in newFileList:
        file.write(line)

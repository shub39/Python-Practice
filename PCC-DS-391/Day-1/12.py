# Write a program to check if a file is empty or not

with open("new_file.txt", "r") as file:
    if file.read() == "":
        print("File is empty")
    else:
        print("File is not empty")

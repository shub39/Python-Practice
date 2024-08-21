# Read Line 4 from test.txt

with open("test.txt", "r") as file:
    print(file.read().split("\n")[4])

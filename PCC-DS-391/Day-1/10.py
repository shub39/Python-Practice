# Write a program to take three names as input from a user in the single input() function call.

input = input("Enter Three names: ")

names = input.split(" ")
index = 1

for i in names:
    print(f"Name {index}: {i}")

# Write a program to create a new string made of an input string’s first, middle, and last character.

name = input("Enter String: ")

# name[0] -> First letter
# name[len(name//2)] -> middle letter
# name[len(name) - 1] -> Last letter
print(f"{name[0]}{name[len(name)//2]}{name[len(name) - 1]}")

# Write a program to create a new string made of the middle three characters of an input string.

name = input("Enter a name: ")
print(name[len(name)//2-1], name[len(name)//2], name[len(name)//2 +1], sep= '')
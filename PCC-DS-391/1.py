# Write a program to accept a string from the user and display characters that are present at an even
# index number. For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

input = input("Enter String: ")

for i in range (0, len(input)):
    if i % 2 == 0:
        print(input[i])

# Write a program to print the cube of all
# numbers from 1 to a given number

number = int(input("Enter Number: "))

for i in range(1, number + 1):
    print(f"Current Number is {i} and the cube is: {i**3}")

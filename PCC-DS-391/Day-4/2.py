# Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    print("Printing Values")
    for index, value in enumerate(args, start=1):
        print(value)

func1(12, 12, 23)
func1(90, 89)

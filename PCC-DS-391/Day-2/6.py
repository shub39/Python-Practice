# Find the factorial of a given number

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

input = int(input("Enter Number: "))
print(factorial(input))

# Reverse a given integer number

number = int(input("Enter number: "))
reverse = 0

while number != 0:
    reverse = (reverse * 10) + (number % 10)
    number //= 10

print(reverse)

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def sum10(a = 0):
    if (a > 10):
        return 0
    return sum10(a + 1) + a

print(sum10())

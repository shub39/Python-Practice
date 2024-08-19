# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current
# and previous number.

first = 0
sum = 0
current = 0
previous = 0

for i in range (0, 11):
    print(f"Current Number {current} Previous Number {previous} Sum: {sum}")
    sum = current + previous
    current+=1
    previous = current - 1

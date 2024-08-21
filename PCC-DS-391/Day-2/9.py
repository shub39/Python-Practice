# Find the sum of the series upto n terms, Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

start = 2
repeat = int(input("Enter Number: "))
sum = start

for i in range (1, repeat):
    sum = sum + ((start * 10) + 2)
    start = (start * 10) + 2

print(sum)

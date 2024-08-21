# Display Fibonacci series up to 10 terms

first = 0
second = 1

print(first)
print(second)
for i in range(8):
    third = first + second
    print(third)
    first = second
    second = third

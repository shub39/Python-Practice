# Write a program to display all prime numbers within a range

range_min = int(input("Enter Starting point: "))
range_max = int(input("Enter Ending point: "))

print(f"Prime Numbers between {range_min} and {range_max} are:")
for i in range(range_min, range_max):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)

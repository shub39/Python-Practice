# Calculate the sum and average of the digits present in a string

str1 = "Pynative29@#8496"
sum = 0
count = 0
for char in str1:
    if char.isdigit():
        sum += int(char)
        count += 1

avg = sum / count
print(f"Sum is: {sum} and Average is: {avg}.")
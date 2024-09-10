# Write a program to count occurrences of all characters within a string.
str1 = "Apple"
count = {}
for char in str1:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
# Removal all characters from a string except integers

str1 = "I am 25 years and 10 months old"
str1_num = ""
for char in str1:
    if char.isnumeric():
        str1_num += char

print(str1_num)
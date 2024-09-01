# Replace each special symbol with # in the following string

str1 = "/* Jon is @developer & musician"
special_char = ['*', '/', '-', '+', '!', '@', '#', '$', '%', '^', '&']

for item in special_char:
    str1 = str1.replace(item, "#")

print(str1)
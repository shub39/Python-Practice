# Remove special symbols / punctuation from a string

str1 = "/* Jon is @developer & musician"
special_char = ['*', '/', '-', '+', '!', '@', '#', '$', '%', '^', '&']

for item in special_char:
    str1 = str1.replace(item, "")

print(str1)
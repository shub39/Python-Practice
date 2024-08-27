# Remove empty strings from a list of strings

str_list = ["Emma", "John", "", "Kelly", None, "Eric", ""]

print("Original list of string is: \n", str_list)
print()

k = []
for item in str_list:
    if item != "" and item != None:
        k.append(item)
print("After removing empty strings\n", k)
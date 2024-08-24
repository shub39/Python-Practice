# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

Char = 0
Digits = 0
Symbol = 0

for char in str1:
    if char.isnumeric():
        Digits += 1
    elif char.isalpha():
        Char += 1
    else:
        Symbol +=  1

print("Total count of digits, chars and symbol is\n")
print("Digits : ", Digits)
print("Char : ", Char)
print("Symbol : ", Symbol)
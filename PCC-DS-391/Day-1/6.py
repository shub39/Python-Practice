# Convert Decimal number to octal using print() output formatting


octal = 0
count = 1
deci = 8
 
while (deci != 0):
    remainder = deci % 8
    octal += remainder * count
    count = count * 10
    deci = deci // 8
print(f'The octal number of decimal number {deci} is {octal}')

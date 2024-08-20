# Write a program to use string.format() method to format the following three variables as per the
# expected output

totalMoney = 3000
quantity = 3
price = 450

string = "I have {} dollars so I can buy {} football for {} dollars"

print(string.format(totalMoney, quantity, float(price)))

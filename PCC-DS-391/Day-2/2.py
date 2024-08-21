# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

a = int(input("Enter a number: "))
s= 0
for i in range(a+1):
  s+=i
print(s)

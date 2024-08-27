# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5

num = int(input("Enter a number: "))
countt = 0

while(num != 0):
    rem = num % 10
    num = num // 10
    countt += 1

print("Total no. of digits is: ",countt)
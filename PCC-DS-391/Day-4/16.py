# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
check = str1.lower()
h = "usa"
c = check.count(h)
print("The USA count is: ", c)
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced 
# if all the characters inthe s1 are present in s2. The character’s position doesn’t matter.

def check(s1, s2):
    if s1 in s2:
        return(True)
    else:
        return(False)

s1 = "Yn"
s2 = "PYnative"
s3 ="Ynf"
c = check(s1, s2)
d = check(s3, s2)
print(c)
print(d)
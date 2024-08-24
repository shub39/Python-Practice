# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first 
# char of s1, then the last char ofs2, Next, the second char of s1 and second last char of 
# s2, and so on. Any leftover chars go at the end of the result.

def s3(s1, s2):
    j = 0
    arrange = ""
    for i in range(len(s1) + len(s2)):
        if i%2 == 0:
            arrange += s1[i//2]
            j -= 1
        else:
            arrange += s2[j]
      
    return arrange
        
s1 = "Abc"
s2 = "Xyz"

c = s3(s1, s2)

print(c)
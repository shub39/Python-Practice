# Append new string in the middle of a given string, Given two strings, s1 and s2. 
# Write a program to create a new strings3 by appending s2 in the middle of s1.

s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")

print(s1[:len(s1)//2], s2, s1[len(s1)//2:], sep= '')
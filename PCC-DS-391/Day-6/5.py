# Write a Python program to remove items 10, 20, 30 from the following set at once.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))
# Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)
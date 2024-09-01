# Use a loop to display elements from a given list present at odd index positions

list1 = [1,2,3,4,5,6,7,8]

print("Elements present in odd index number is:")
for i in range( len(list1)):
    if i % 2 != 0:
        print(f"{list1[i]} present at index position {i}")
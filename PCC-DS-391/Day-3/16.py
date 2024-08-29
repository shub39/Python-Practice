# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5 
# 4 4 4 4 5
# 5 5 5 5 5

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end= " ")
    for k in range(i+1, 6):
        print(k, end= " ")
    print()
# 1
# 2 1
# 4 2 1 
# 8 4 2 1
# 16 8 4 2 1
# 32 16 8 4 2 1 
# 64 32 16 8 4 2 1 
# 128 64 32 16 8 4 2 1 

for i in range(1, 9):
  for j in range(i, 0, -1):
    print(2 ** (j-1), end= " ")
  print()
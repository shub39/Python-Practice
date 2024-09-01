#         1
#       1 2
#     1 2 3
#   1 2 3 4 
# 1 2 3 4 5 

for i in range(1,6):
    print("  "*(5-i), *range(1,1+i))
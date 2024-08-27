#   e. 1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5

for i in range(5):
    a=''
    for j in range(i+1):
        a += str(j+1) +' '
    print(a)

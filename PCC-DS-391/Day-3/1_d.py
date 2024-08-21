# d. 0 1 2 3 4 5
#    0 1 2 3 4
#    0 1 2 3
#    0 1 2 
#    0 1


n=6
for i in range(5):
    a=''
    for j in range(n-i):
        a += str(j) + ' '
    print(a)

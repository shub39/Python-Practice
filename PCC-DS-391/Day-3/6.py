# e. 1 1 1 1 1
#    2 2 2 2
#    3 3 3
#    4 4
#    5

n=5
for i in range(5):
    b=''
    for j in range(n-i):
        a = i+1
        b += str(a)+' '
    print(b)

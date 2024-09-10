  # 1 
  # 1 1
  # 1 2 1 
  # 1 3 3 1
  # 1 4 6 4 1
  # 1 5 10 10 5 1
  # 1 6 15 20 15 6 1 

  
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

for i in range(1,8):
    for j in range(0,i):
      if j==0 or j==i-1:
        print(1,end=" ")
      else:
        print(fact(i-1)//(fact(j)*fact(i-1-j)),end=" ")
    print()
    print("") 

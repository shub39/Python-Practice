# 1
# 3 2
# 6 5 4
# 10 9 8 7

start = 1
stop = 2
current_Number = stop
for i in range(2, 6):
    for j in range(start, stop):
      current_Number -= 1
      print(current_Number, end=' ')
    print("")
    
    start = stop
    stop += i
    current_Number = stop
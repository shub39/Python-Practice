# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2 
# 1

number = 5
i = 5

for j in range(1, 6):
    print(f"{str(number)} " * i)
    number = 5 - j
    i -= 1

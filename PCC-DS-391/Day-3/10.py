# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

number = 1
i = 1

for j in range(0, 5):
    print(f"{str(number)} " * i)
    number += 2
    i += 1

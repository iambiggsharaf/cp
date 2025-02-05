t = int(input())
for _ in range(t):
    n = input()
    s = input()
    x, y = 0, 0
    flag = False
    for i in s:
        if i == "L": x -= 1
        if x == 1 and y == 1: flag = True
        if i == "R": x += 1
        if x == 1 and y == 1: flag = True
        if i == "U": y += 1
        if x == 1 and y == 1: flag = True
        if i == "D": y -= 1
        if x == 1 and y == 1: flag = True
    if flag: print("YES")
    else: print("NO")

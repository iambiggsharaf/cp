t = int(input())
for _ in range(t):
    s = input()
    a = 0
    b = 0
    for i in s:
        if i == "A": a+=1
        if i == "B": b+=1
    if a >= b: print("A")
    else: print("B")
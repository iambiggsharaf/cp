t = int(input())
for _ in range(t):
    n = int(input())
    a, b = input(), input()
    a = a.replace("G", "B")
    b = b.replace("G", "B")
    if a == b: print("YES")
    else: print("NO")
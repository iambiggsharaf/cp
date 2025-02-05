t = int(input())
for _ in range(t):
    n = int(input())
    foo = [int(i) for i in input().split()]
    a, b = 0, 0
    for i in foo:
        if i % 2 == 0: a += 1
        else: b += 1
    if a == b: print("YES")
    else: print("NO")
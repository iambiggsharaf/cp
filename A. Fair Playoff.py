t = int(input())
for _ in range(t):
    foo = [int(i) for i in input().split()]
    a = max(foo[0], foo[1])
    b = max(foo[2], foo[3])
    c = sorted([a, b])
    a = c[0]
    b = c[1]
    foo.sort()
    if a == foo[2] and b == foo[3]:
        print("YES")
    else:
        print("NO")
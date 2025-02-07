t = int(input())
for _ in range(t):
    foo = []
    for _ in range(4):
        a, b = [int(i) for i in input().split()]
        foo.append((a, b))
    foo.sort()
    # print(foo)
    print((foo[1][1] - foo[0][1])**2)
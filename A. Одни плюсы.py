t = int(input())
for _ in range(t):
    foo = sorted([int(i) for i in input().split()])
    foo[0] += 1
    foo.sort()
    foo[0] += 1
    foo.sort()
    foo[0] += 1
    foo.sort()
    foo[0] += 1
    foo.sort()
    foo[0] += 1
    foo.sort()
    print(foo[0]*foo[1]*foo[2])
    
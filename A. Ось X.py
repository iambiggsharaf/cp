t = int(input())
for _ in range(t):
    foo = sorted([int(i) for i in input().split()])
    print(abs(foo[0]-foo[2]))
    
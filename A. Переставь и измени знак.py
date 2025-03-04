t = int(input())
for _ in range(t):
    n = int(input())
    foo = sum([abs(int(i)) for i in input().split()])
    print(foo)
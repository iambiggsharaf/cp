t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    n -= y
    print((n//x)*x + y)
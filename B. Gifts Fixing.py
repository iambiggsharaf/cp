t = int(input())
for _ in range(t):
    n = int(input())
    foo = [int(i) for i in input().split()]
    bar = [int(i) for i in input().split()]
    cnt, a, b = 0, min(foo), min(bar)
    for i in range(n): cnt += max(foo[i]-a, bar[i]-b)
    print(cnt)
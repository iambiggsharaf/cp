t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    cnt = 0
    foo = [0]+[int(i) for i in input().split()]
    for i in range(n):
        cnt = max(cnt, foo[i+1]-foo[i])
    cnt = max(cnt, (x - foo[n])*2)
    print(cnt)
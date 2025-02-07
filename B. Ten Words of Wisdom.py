t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    ans = 0
    for j in range(n):
        a, b = [int(i) for i in input().split()]
        if b > cnt and a <= 10:
            cnt = b
            ans = j + 1
    print(ans)

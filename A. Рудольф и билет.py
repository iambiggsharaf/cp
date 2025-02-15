t = int(input())
for _ in range(t):
    n, m, k = [int(i) for i in input().split()]
    foo = [int(i) for i in input().split()]
    bar = [int(i) for i in input().split()]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if foo[i] + bar[j] <= k: cnt += 1
    print(cnt)
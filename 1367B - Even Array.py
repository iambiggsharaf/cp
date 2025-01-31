t = int(input())
for _ in range(t):
    n = int(input())
    foo = [int(x) for x in input().split()]
    if n % 2 == 0: a, b = n // 2, n // 2
    else: a, b = n // 2 + 1, n // 2
    cnt, cnt1 = 0, 0
    for i in foo:
        if i % 2 == 0: a -= 1
        else: b -= 1
    if a > 0 or b > 0: print(-1)
    else:
        for i in range(n):
            if (foo[i] % 2 == 0) != (i % 2 == 0): cnt += 1
        print(cnt // 2)

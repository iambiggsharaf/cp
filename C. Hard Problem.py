t = int(input())
for _ in range(t):
    m, a, b, c = [int(i) for i in input().split()]
    cnt = min(m, a) + min(m, b)
    cnt += min(c, ((m - min(m, a)) + (m - (min(m, b)))))
    print(cnt)
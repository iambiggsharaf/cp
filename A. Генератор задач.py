t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    s = input().lower()
    a, b, c, d, e, f, g = 0,0,0,0,0,0,0
    a = s.count('a')
    b = s.count('b')
    c = s.count('c')
    d = s.count('d')
    e = s.count('e')
    f = s.count('f')
    g = s.count('g')
    cnt = 0
    if a < m: cnt += m - a
    if b < m: cnt += m - b
    if c < m: cnt += m - c
    if d < m: cnt += m - d
    if e < m: cnt += m - e
    if f < m: cnt += m - f
    if g < m: cnt += m - g
    print(cnt)
    
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    a = n // 10000 * 10000
    if a != 0: cnt += 1
    b = n % 10000 // 1000 * 1000
    if b != 0: cnt += 1
    c = n % 1000 // 100 * 100
    if c != 0: cnt += 1
    d = n % 100 // 10 * 10
    if d != 0: cnt += 1
    e = n % 10
    if e != 0: cnt += 1
    print(cnt)
    if a != 0: print(a, end=" ")
    if b != 0: print(b, end=" ")
    if c != 0: print(c, end=" ")
    if d != 0: print(d, end=" ")
    if e != 0: print(e, end=" ")
    print()
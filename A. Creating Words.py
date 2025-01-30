t = int(input())
for _ in range(t):
    a, b = input().split()
    a, b = list(a), list(b)
    a[:1], b[:1] = b[:1], a[:1]
    print("".join(a), "".join(b))
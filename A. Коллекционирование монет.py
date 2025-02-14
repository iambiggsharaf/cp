t =  int(input())
for _ in range(t):
    a, b, c, n = [int(i) for i in input().split()]
    n -= ((max(a, b, c) - a) + (max(a, b, c) - b) + (max(a, b, c) - c))
    if n >= 0 and n % 3 == 0: print("YES")
    else: print("NO")
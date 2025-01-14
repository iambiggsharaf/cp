t = int(input())
for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    if a + b == c: print("+")
    else: print("-")
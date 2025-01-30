t = int(input())
for _ in range(t):
    n = int(input())
    a = n // 3
    b = n - a
    if b % 2 == 0:
        print(a, b//2)
    else:
        print(a+1, (b-1)//2)
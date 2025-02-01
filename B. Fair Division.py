from math import ceil, floor
t = int(input())
for _ in range(t):
    n = int(input())
    n = min(abs(n - (ceil(n / 3)*3)), abs(n - (floor(n / 3)*3)))
    if n == 1:
        print("First")
    else:
        print("Second")
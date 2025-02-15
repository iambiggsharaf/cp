t = int(input())
for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    if c % 2 == 0:
        if a == b: print("Second")
        elif a > b: print("First")
        elif a < b: print("Second")
    if c % 2 != 0:
        if a == b: print("First")
        elif a > b: print("First")
        elif a < b: print("Second")
    
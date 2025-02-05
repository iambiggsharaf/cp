t = int(input())
for _ in range(t):
    for _ in range(8):
        for i in input():
            if i != '.': print(i, end="")
    print()
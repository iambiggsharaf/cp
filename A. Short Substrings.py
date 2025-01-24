t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n == 2:
        print(s)
    else:
        print(s[0] + s[1::2])
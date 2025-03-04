t = int(input())
for _ in range(t):
    n = input()
    if len(n) < 3:
        print("NO")
    elif len(n) == 3:
        if n[0] == '1' and n[1] == '0' and n[2] > '1':
            print("YES")
        else:
            print("NO")
    elif len(n) > 3:
        if n[0] == '1' and n[1] == '0' and n[2] >= '1':
            print("YES")
        else:
            print("NO")
    
t = int(input())
for i in range(t):
    n = int(input())
    foo = [int(x) for x in input().split()]
    flag = True
    for j in range(n):
        if foo[j] <= j * 2 or foo[j] <= (n - j - 1) * 2:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    n = int(input())
    foo = [int(i) for i in input().split()]
    foo.sort()
    flag = True
    for i in range(n - 1):
        if abs(foo[i] - foo[i + 1]) > 1:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
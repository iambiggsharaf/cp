t = int(input())
for _ in range(t):
    n = int(input())
    foo = [int(i) for i in input().split()]
    cnt = sum([i for i in foo if i % 2 == 0])
    b = [i for i in foo if i % 2 != 0]
    cnt1 = 0
    flag = True
    for i in b:
        cnt1 += i
        if cnt <= cnt1:
            flag = False
    if flag: print("YES")
    else: print("NO")
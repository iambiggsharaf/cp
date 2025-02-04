t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    foo = [int(i) for i in input().split()]
    if k in foo:
        print("YES")
    else: print("NO")
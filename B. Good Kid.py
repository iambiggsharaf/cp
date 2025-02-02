t = int(input())
for _ in range(t):
    n = int(input())
    foo = [int(i) for i in input().split()]
    foo.sort()
    foo[0] += 1
    cnt = 1
    for i in foo:
        cnt *= i
    print(cnt)
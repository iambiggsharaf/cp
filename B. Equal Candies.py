t = int(input())
for _ in range(t):
    n = int(input())
    foo = sorted([int(i) for i in input().split()])
    cnt = 0
    for i in foo:
        cnt += i - foo[0]
    print(cnt)        
    
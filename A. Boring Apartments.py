foo = [str(i) for i in range(1, 10) for i in (i*1, i*11, i*111, i*1111)]
t = int(input())
for _ in range(t):
    n = input()
    cnt = len(n)
    for i in foo:
        if i != n: cnt += len(i)
        else: break
    print(cnt)
n, cnt = int(input()), 0
foo = [int(i) for i in input().split()]
minn = foo[0]
maxx = foo[0]
for i in foo:
    if i > maxx:
        cnt += 1
        maxx = i
    if i < minn:
        cnt += 1
        minn = i
print(cnt)
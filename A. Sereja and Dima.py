n = int(input())
foo = [int(i) for i in input().split()]
cnt1 = 0
cnt2 = 0

for i in range(n):
    if i % 2 == 0:
        if foo[0] >= foo[len(foo)-1]:
            cnt1 += foo[0]
            foo = foo[1:]
        else:
            cnt1 += foo[len(foo) - 1]
            foo = foo[:-1]
    else:
        if foo[0] >= foo[len(foo)-1]:
            cnt2 += foo[0]
            foo = foo[1:]
        else:
            cnt2 += foo[len(foo) - 1]
            foo = foo[:-1]
print(cnt1, cnt2)
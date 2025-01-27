n = int(input())
foo = [int(x) for x in input().split()]
ans = {}
for i in range(n):
    if foo[i] not in ans:
        ans[foo[i]] = [i + 1]
    else:
        ans[foo[i]].append(i + 1)
min_length = min(len(lst) for lst in ans.values())
if len(ans) < 3:
    print(0)
    exit()
print(min_length)
for i in range(min_length):
    print(ans[1][i], ans[2][i], ans[3][i])
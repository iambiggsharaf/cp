ans = [int(i) for i in input().split()]
ans.insert(0, 0)
s = input()
cnt = 0
for i in s:
    cnt += ans[int(i)]
print(cnt)
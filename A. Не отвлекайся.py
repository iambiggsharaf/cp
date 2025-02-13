t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = {key: True for key in s}
    flag = True
    for i in range(n-1):
        if ans[s[i]] == False:
            flag = False
            break
        if s[i]!=s[i+1]:
            ans[s[i]] = False
    if ans[s[-1]] == False:
        flag = False
    if flag: print("YES")
    else: print("NO")
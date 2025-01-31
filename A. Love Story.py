t = int(input())
for _ in range(t):
    s, cnt = input(),0
    for i in range(len(s)): 
        if s[i]!="codeforces"[i]: cnt+=1
    print(cnt)
s = 'a'+input()
cnt = 0
for i in range(len(s)-1):
    cnt += min(abs(ord(s[i])-ord(s[i+1])), 26 - abs(ord(s[i])-ord(s[i+1])))
print(cnt)
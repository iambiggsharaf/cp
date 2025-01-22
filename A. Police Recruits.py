n = int(input())
foo = list(map(int, input().split()))
cnt = 0
score = 0
for i in foo:
    if i > 0: 
        if score <= 0: score = i
        else: score += i
    else: score += i
    if score < 0: cnt+=1
    # print(score, cnt)
print(cnt)



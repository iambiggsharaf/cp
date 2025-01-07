n, k = [int(i) for i in input().split()]
cnt = 0
time = 240 - k
for i in range(1, n + 1):
    if 5 * i <= time:
        cnt += 1
        time -= 5 * i
    else: break
print(cnt)
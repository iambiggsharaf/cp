k, r = [int(i) for i in input().split()]
cnt = 1
while True:
    number = (k * cnt)
    mod = 10
    if number % mod == r or number % mod == 0:
        print(cnt)
        break
    cnt += 1
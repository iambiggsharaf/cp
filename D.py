t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arrays = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        s = sum(arr)
        f = 0
        multiplier = m
        for a in arr:
            f += a * multiplier
            multiplier -= 1
        arrays.append((s, f))
    
    arrays.sort(key=lambda x: x[0], reverse=True)
    
    prefix = 0
    ans = 0
    for s, f in arrays:
        ans += f + prefix * m
        prefix += s
    print(ans)

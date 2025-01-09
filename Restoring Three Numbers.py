a, b, c, d = [int(i) for i in input().split()]
maxx = max(a, b, c, d)
if a != maxx: print(maxx - a, end=" ")
if b != maxx: print(maxx - b, end=" ")
if c != maxx: print(maxx - c, end=" ")
if d != maxx: print(maxx - d, end=" ")
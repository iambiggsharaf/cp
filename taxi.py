from math import *

n, cnt = int(input()), 0
foo = [int(i) for i in input().split()]
a, b, c, d = foo.count(1), foo.count(2), foo.count(3), foo.count(4)

cnt += d

temp = min(a, c)
cnt += temp
a -= temp
c -= temp

temp = min(ceil(a/2), b)
cnt += temp
a -= temp * 2
b -= temp

cnt += c
cnt += ceil(b / 2)
cnt += ceil(a / 4)

print(cnt)

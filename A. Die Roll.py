from math import gcd

a, b = map(int, input().split())
a = 7 - max(a, b)
b = 6

print(a // gcd(a, b), '/', b // gcd(a, b), sep='')
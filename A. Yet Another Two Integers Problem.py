from math import *
t = int(input())
for _ in range(t):
    a, b = [int(i) for i in input().split()]
    print(int(ceil(abs(a - b) / 10)))
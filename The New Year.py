x, y, z = [int(i) for i in input().split()]
a = abs(x-y) + abs(x-z)
b = abs(y-x) + abs(y-z)
c = abs(z-x) + abs(z-y)
print(min(a, b, c))
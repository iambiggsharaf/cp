t = int(input())
for _ in range(t):
    n, a, b = [int(i) for i in input().split()]
    b = min(2*a, b)
    n = (n//2)*b + (n%2)*a
    print(n)
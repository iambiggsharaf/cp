t = int(input())
for _ in range(t):
    n = int(input())
    print(n//4+((n-(n//4*4))//2))
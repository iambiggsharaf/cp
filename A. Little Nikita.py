t = int(input())
for _ in range(t):
    a, b = [int(i) for i in input().split()]
    if a < b:
        print("No")
    elif a == b: 
        print("Yes")
    elif a > b and (a - b) % 2 == 0:
        print("Yes")
    else:
        print("No")

t = int(input())
foo = [0]+[int(i) for i in range(2000) if int(i) % 3 !=0 and int(i) % 10 != 3]
for _ in range(t):
    print(foo[int(input())])   
t = int(input())
for i in range(t):
    n = int(input())
    foo = reversed([input() for _ in range(n)])
    for i in foo:
        print(i.find('#')+1, end=" ")

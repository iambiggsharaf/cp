
foo = []
num = 1
i = 0
step = 1
ss = 1
while num <= 10**10:
    # print(num, end=" ")
    foo.append(num)
    num+=step
    i+=1
    if i == 9:
        step += 10**ss
        num += 1
        ss+=1
        i = 0
# print(len(foo))

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(90):
        if foo[i] == n:
            print(i+1)
            break
        elif foo[i] > n:
            print(i)
            break
        
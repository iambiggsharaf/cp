t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    n = s.rfind('B') - s.find('B') + 1
    print(n)

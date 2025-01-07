foo = [1]
for i in range(1, 33):
    foo.append(2 ** i + (foo[i - 1]))
foo = foo[1:]
t = int(input())
for _ in range(t):
    n = int(input())
    for i in foo:
        if n % i == 0:
            print(n // i)
            break
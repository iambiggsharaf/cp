t = int(input())
for _ in range(t):
    foo = [list(input()) for _ in range(10)]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if foo[i][j] == 'X':
                if ((i == 0 or i == 9) and 0 <= j <= 9) or ((j == 0 or j == 9) and 0 <= i <= 9): cnt += 1

                if ((i == 1 or i == 8) and 1 <= j <= 8) or ((j == 1 or j == 8) and 1 <= i <= 8): cnt += 2

                if ((i == 2 or i == 7) and 2 <= j <= 7) or ((j == 2 or j == 7) and 2 <= i <= 7): cnt += 3

                if ((i == 3 or i == 6) and 3 <= j <= 6) or ((j == 3 or j == 6) and 3 <= i <= 6): cnt += 4

                if ((i == 4 or i == 5) and 4 <= j <= 5) or ((j == 4 or j == 5) and 4 <= i <= 5): cnt += 5
    print(cnt)

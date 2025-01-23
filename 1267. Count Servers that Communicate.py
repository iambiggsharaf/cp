# grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
grid = [[1,0],[0,1]]

ans = []
for i in range(len(grid[0])):
    ans.append([])
    for j in range(len(grid)):
        ans[-1].append(grid[j][i])
# print(*ans, sep='\n')

cnt = 0

for i in range(len(grid)):
    if sum(grid[i]) > 1:
        cnt += sum(grid[i])
    else:
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if sum(ans[j]) > 1:
                    cnt += 1
# print(cnt)
return cnt
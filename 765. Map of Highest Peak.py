# foo = [[0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0]]
# foo = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
foo = [[0],[0],[0],[0],[1],[0],[0],[1],[1]]

n = len(foo)
m = len(foo[0])
ans = [[-1]*(m) for _ in range(n)]
nums = []
for i in range(n):
    for j in range(m):
        if foo[i][j] == 1: 
            ans[i][j] = 0
            nums.append((i,j))
print(*ans, sep="\n")
print()
while len(nums) > 0:
    i,j = nums.pop(0)
    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
        if 0 <= i + x < n and 0 <= j + y < m and ans[i+x][j+y] == -1:
            ans[i+x][j+y] = ans[i][j] + 1
            nums.append((i+x,j+y))
    print(*ans, sep="\n")
    print()
    




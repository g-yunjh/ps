n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
res = []

def dfs(x, y):
    visited[x][y] = 1
    cnt = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1 and not visited[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt

for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and not visited[i][j]:
            res.append(dfs(i,j))

print(len(res))
for x in sorted(res):
    print(x)
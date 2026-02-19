N = int(input())
grid = [list(input()) for _ in range(N)]

def dfs(grid, x, y, visited):
    global cnt
    visited[x][y] = True
    cnt += 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny] == '1':
                dfs(grid, nx, ny, visited)

visited = [[False]*N for _ in range(N)]
danji = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and not visited[i][j]:
            cnt = 0
            dfs(grid, i, j, visited)
            danji.append(cnt)
danji.sort()
print(len(danji))
for d in danji:
    print(d)
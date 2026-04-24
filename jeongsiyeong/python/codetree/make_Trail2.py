N, K = map(int, input().split())

grid = []
answer = 0
top = 0

dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]

def is_range(r, c):
    global N
    return 0<=r<N and 0<=c<N

def dfs(r, c, cut_limit, cur_cnt):
    global top, answer
    answer = max(answer, cur_cnt)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if is_range(nr, nc) and not visited[nr][nc]:
            if grid[nr][nc] < grid[r][c]:
                visited[nr][nc] = True
                dfs(nr, nc, cut_limit, cur_cnt+1)
                visited[nr][nc] = False
            else:
                if grid[nr][nc] != top and grid[r][c] != 1:
                    temp = grid[nr][nc]
                    needed = grid[nr][nc] - grid[r][c] + 1
                    if needed <= cut_limit:
                        grid[nr][nc] = grid[r][c] - 1
                        visited[nr][nc] = True
                        dfs(nr, nc, cut_limit - needed, cur_cnt+1)
                        visited[nr][nc] = False
                        grid[nr][nc] = temp

for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if top < line[c]:
            top = line[c]
    grid.append(line)
    
for r in range(N):
    for c in range(N):
        if grid[r][c] == top:
            visited = [[False] * N for _ in range(N)]
            visited[r][c] = True
            dfs(r, c, K, 1)

print(answer)
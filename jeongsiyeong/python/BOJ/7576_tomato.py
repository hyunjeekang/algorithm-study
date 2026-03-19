from collections import deque

M, N = map(int, input().split()) # M: cols, N: rows
grid = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
dist = [[-1] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 1:
            queue.append((r, c))
            dist[r][c] = 0  

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

max_days = 0

while queue:
    curr_r, curr_c = queue.popleft()
    
    for i in range(4):
        nr, nc = curr_r + dr[i], curr_c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
            grid[nr][nc] = 1
            dist[nr][nc] = dist[curr_r][curr_c] + 1
            max_days = max(max_days, dist[nr][nc])
            queue.append((nr, nc))

for row in grid:
    if 0 in row:
        print(-1)
        exit()

print(max_days)
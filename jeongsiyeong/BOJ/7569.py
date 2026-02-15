from collections import deque

M, N, H = map(int, input().split()) # M: cols, N: rows
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
dist = [[[-1] * M for _ in range(N)] for _ in range(H)]

for z in range(H):
    for r in range(N):
        for c in range(M):
            if grid[z][r][c] == 1:
                queue.append((z, r, c))
                dist[z][r][c] = 0  

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dz = [1, -1]

max_days = 0

while queue:
    curr_z, curr_r, curr_c = queue.popleft()
    
    for i in range(4):
        nr, nc = curr_r + dr[i], curr_c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M and grid[curr_z][nr][nc] == 0:
            grid[curr_z][nr][nc] = 1
            dist[curr_z][nr][nc] = dist[curr_z][curr_r][curr_c] + 1
            max_days = max(max_days, dist[curr_z][nr][nc])
            queue.append((curr_z, nr, nc))
    for i in range(2):
        nz = curr_z + dz[i]

        if 0<=nz<H and grid[nz][curr_r][curr_c] == 0:
            grid[nz][curr_r][curr_c] = 1
            dist[nz][curr_r][curr_c] = dist[curr_z][curr_r][curr_c] + 1
            max_days = max(max_days, dist[nz][curr_r][curr_c])
            queue.append((nz,curr_r,curr_c))
for z in range(H):
    for r in range(N):
        if 0 in grid[z][r]: # grid[z][r]은 1차원 리스트이므로 in 연산자 사용 가능
            print(-1)
            exit()

print(max_days)
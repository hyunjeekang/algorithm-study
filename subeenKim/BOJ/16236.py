from collections import deque
N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]

def find_start(grid, N):
    cnt = 0
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 9:
                grid[x][y] = 0
                return x, y

def bfs():
    global baby, time, ate
    q = deque([(sx, sy, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    candidates = []
    min_dist = float('inf')

    while q:
        x, y, cnt = q.popleft()
        if cnt >= min_dist:
            break

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and ocean[nx][ny] <= baby:
                visited[nx][ny] = True
                if 0 < ocean[nx][ny] < baby :
                    candidates.append((nx, ny, cnt+1))
                    min_dist = cnt+1
                else :
                    q.append((nx, ny, cnt+1))
    return candidates
                    
baby, ate, total_time = 2, 0, 0
sx, sy = find_start(ocean, N)

while True :
    candidates = bfs()
    if not candidates :
        break

    candidates.sort()
    sx, sy, cnt = candidates[0]
    total_time += cnt
    ocean[sx][sy] = 0

    ate += 1
    if ate == baby :
        baby += 1
        ate = 0

print(total_time)
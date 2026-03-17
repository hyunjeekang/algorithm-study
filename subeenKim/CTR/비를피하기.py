from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def bfs(r, c):
    visited = [[-1]*n for _ in range(n)]
    q = deque([(r, c)])
    visited[r][c] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if grid[nx][ny] == 0 or grid[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif grid[nx][ny] == 3:
                    ans[r][c] = visited[x][y] + 1
                    return
    
    ans[r][c] = -1
    return

ans = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if grid[r][c] == 2:
            bfs(r, c)

for x in ans:
    print(*x)
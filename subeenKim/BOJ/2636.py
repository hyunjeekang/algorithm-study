from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cheese_cnt = 0
time = 0
for x in range(1, N-1):
    for y in range(1, M-1):
        if grid[x][y] == 1:
            cheese_cnt += 1

while True :
    q = deque([(0, 0)])
    time += 1
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    melt_list = []
    while q :
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                elif grid[nx][ny] == 1:
                    melt_list.append((nx, ny))
                visited[nx][ny] = True

    if cheese_cnt == len(melt_list):
        print(time)
        print(cheese_cnt)
        break
    else :
        cheese_cnt -= len(melt_list)
        for r, c in melt_list:
            grid[r][c] = 0
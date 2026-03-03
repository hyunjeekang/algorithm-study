from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
pic_cnt = 0
max_pic_area = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            pic_cnt += 1
            pic_area = 1
            visited[i][j] = True
            q = deque([(i, j)])

            while q :
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                        pic_area += 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
            max_pic_area = pic_area if pic_area > max_pic_area else max_pic_area

print(pic_cnt)
print(max_pic_area)
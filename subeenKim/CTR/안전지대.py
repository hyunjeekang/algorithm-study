# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.
# def dfs(grid, x, y, visited):
#     visited[x][y] = True

#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         nx, ny = x+dx, y+dy
#         if 0 <= nx < n and 0 <= ny < m:
#             if not visited[nx][ny] and grid[nx][ny] > k:
#                 visited[nx][ny] = True
#                 dfs(grid, nx, ny, visited)
# safe_dict = {}
# max_height = 0
# for x in grid :
#     max_height = max(x) if max(x) > max_height else max_height
# for k in range(1, max_height+1):
#     cnt = 0
#     visited = [[False]*m for _ in range(n)]
#     for x in range(n):
#         for y in range(m):
#             if grid[x][y] > k and not visited[x][y]:
#                 cnt += 1
#                 dfs(grid, x, y, visited)
#             safe_dict[k] = cnt
# safe_list = sorted(safe_dict.items(), key = lambda x: (-x[1], x[0]))
# print(safe_list[0][0], safe_list[0][1])

from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_height = 0
for g in grid:
    max_height = max(g) if max(g) > max_height else max_height
def get_safezone(k):
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and grid[nx][ny] > k:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    return cnt

max_cnt, max_k = -1, -1
for k in range(1, max_height+1):
    current_cnt = get_safezone(k)
    if current_cnt > max_cnt:
        max_cnt = current_cnt
        max_k = k
print(max_k, max_cnt)
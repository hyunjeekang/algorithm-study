from collections import deque

dr = [0, 1, 0, -1]; dc = [1, 0, -1, 0]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

visited = [[0] * n for _ in range(n)] # 방문정보

Q = deque()
#  문제는 행과 열의 크기가 1 부터 n까지, 시작점의 좌표를 0 에서 n-1 범위로 변환
for r, c in points:
    Q.append((r-1, c-1))
    visited[r-1][c-1] = 1

while Q:
    r, c = Q.popleft()
    # 인접한 네곳을 확인
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 경계 체크
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        # 길이 아니거나 길인데 방문했으면
        if grid[nr][nc] == 1 or visited[nr][nc] == 1:
            continue
        visited[nr][nc] = 1
        Q.append((nr, nc))

ans = 0
for r in range(n):
    for c in range(n):
        if visited[r][c] == 1:
            ans += 1

print(ans)



# from collections import deque

# n,k = tuple(map(int,input.split())) 
# grid = [
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# bfs_q = deque()
# visited = [
#     [False for _ in range(n)]
#     for _ in range(n)
# ]

# def in_range(x,y):
#     return 0 <= x < n and 0 <= y < n

# def can_go(x,y):
#     return in_range(x,y) and not grid[x][y] and not visited[x][y]
# def bfs():
#     while bfs_q:
#         x,y = bfs_q.popleft()

#         dxs,dys = [1,-1,0,0],[0,0,1,-1]

#         for dx,dy in zip(dxs,dys):
#             nx,ny = x+dx, y+dy

#             if can_go(nx,ny):
#                 bfs_q.append((nx,ny))
#                 visited[nx][ny] = True

# # 시작점을 모두 bfs queue에 넣습니다.
# for _ in range(k):
#     x, y = tuple(map(int, input().split()))
#     bfs_q.append((x - 1, y - 1))
#     visited[x - 1][y - 1] = True

# # bfs를 진행합니다.
# bfs()

# ans = sum([
#     1
#     for i in range(n)
#     for j in range(n)
#     if visited[i][j]
# ])

# print(ans)
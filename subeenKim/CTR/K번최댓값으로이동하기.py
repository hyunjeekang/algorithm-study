from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1
# Please write your code here.

def bfs(n, graph, X, Y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(X, Y)])
    visited = [[False]*n for _ in range(n)]
    visited[X][Y] = True
    candidates = [] # 도달 가능한 (값, 행, 열)
    
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                if not visited[nx][ny] and graph[X][Y] > graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    candidates.append((graph[nx][ny], nx, ny))

    if not candidates :
        return None
    # 정렬 : 값 (큰거), 행 (작은거), 열 (작은거)
    candidates.sort(key=lambda x: (-x[0], x[1], x[2]))
    return candidates[0][1], candidates[0][2]

for _ in range(k):
    next_pos = bfs(n, grid, r, c)
    if not next_pos :
        break
    r, c = next_pos

print(r+1, c+1)
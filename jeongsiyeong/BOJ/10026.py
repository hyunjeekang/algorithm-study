from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    current_color = arr[r][c] # 시작점의 색상

    while q:
        cur_r, cur_c = q.popleft()
        
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n:
                # 방문하지 않았고, 같은 색상이라면 큐에 추가
                if not visited[nr][nc] and arr[nr][nc] == current_color:
                    visited[nr][nc] = True
                    q.append((nr, nc))

# 1. 적록색약이 아닌 경우 (Normal)
normal_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            normal_cnt += 1

# 2. 적록색약인 경우를 위해 세팅 변경
# 'G'를 모두 'R'로 변경하여 R과 G를 통합
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

# visited 배열 초기화 (refresh)
visited = [[False]*n for _ in range(n)]

# 3. 적록색약인 경우 (Blind) 탐색
blind_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            blind_cnt += 1

print(normal_cnt, blind_cnt)
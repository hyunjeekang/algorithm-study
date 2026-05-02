from collections import deque

dc = [-1, -1, -1, 0, 0, 1, 1, 1]
dr = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    
    while queue:
        cur_r, cur_c = queue.popleft()
        
        for i in range(8):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != '*':
                visited[nr][nc] = True
                if mine_counts[nr][nc] == 0:
                    queue.append((nr, nc))

T = int(input())
for tc in range(1, T + 1):

    N = int(input())

    arr = [list(input()) for _ in range(N)]
    
    visited = [[False] * N for _ in range(N)]
    mine_counts = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '*':
                continue
            
            count = 0
            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '*':
                    count += 1
            mine_counts[r][c] = count
            
    ans = 0
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '*' and mine_counts[r][c] == 0 and not visited[r][c]:
                ans += 1
                bfs(r, c)
                
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '*' and not visited[r][c]:
                ans += 1
                
    print(f"#{tc} {ans}")
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)] 

visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]


q = deque([(0, 0, K, 1)])
visited[0][0][K] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = -1

while q:
    r, c, chance, dist = q.popleft()
    
    if r == N - 1 and c == M - 1:
        answer = dist
        break

    is_day = (dist % 2 != 0)
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '0' and visited[nr][nc][chance] == 0:
                visited[nr][nc][chance] = dist + 1
                q.append((nr, nc, chance, dist + 1))
            
            elif arr[nr][nc] == '1' and chance > 0 and visited[nr][nc][chance - 1] == 0:
                if is_day:
                    visited[nr][nc][chance - 1] = dist + 1
                    q.append((nr, nc, chance - 1, dist + 1))
                else:
                    q.append((r, c, chance, dist + 1))

print(answer)
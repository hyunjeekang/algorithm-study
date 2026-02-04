#백준 2468 안전영역
from collections import deque
def is_range(r,c,max_r,max_c):
    return r>=0 and r<max_r and c>=0 and c<max_c

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]

max_count = 0
max_n = -1
for col in field:
    max_n = max(max_n, max(col))

for height in range(max_n+1):
    visited = [[False for _ in range(N)] for _ in range(N)]  
    area_count = 0
    #각 높이마다 bfs 탐색
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and field[r][c] > height:
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                area_count+=1
                while q:
                    cur_r, cur_c = q.popleft()
                    

                    for dir in range(4):
                        nr = cur_r + dr[dir]
                        nc = cur_c + dc[dir]

                        if is_range(nr, nc, N, N):
                            if not visited[nr][nc] and field[nr][nc] > height:
                                visited[nr][nc] = True
                                q.append((nr, nc))
    max_count = max(area_count, max_count)            
print(max_count)

from collections import deque
import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())
Lands = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while True:
    is_moved = False 
    visited = [[False]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                
                union = [(r, c)] 
                tot_pop = Lands[r][c]
                
                while q:
                    curr_r, curr_c = q.popleft()
                    
                    for i in range(4):
                        nr = curr_r + dr[i]
                        nc = curr_c + dc[i]
                        
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            if L <= abs(Lands[curr_r][curr_c] - Lands[nr][nc]) <= R:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                                union.append((nr, nc))
                                tot_pop += Lands[nr][nc] 

                if len(union) >= 2:
                    is_moved = True 
                    avg_pop = tot_pop // len(union)
                    for ur, uc in union:
                        Lands[ur][uc] = avg_pop
    
    if not is_moved:
        break
        
    ans += 1

print(ans)
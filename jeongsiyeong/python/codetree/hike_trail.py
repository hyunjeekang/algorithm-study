
def dfs(r, c, remaining_k, dist):
    global answer
 
    if dist > answer:
        answer = dist
    
    visited[r][c] = True
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
     
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            
       
            if grid[nr][nc] < grid[r][c]:
                dfs(nr, nc, remaining_k, dist + 1)
            

            else:
              
                if grid[nr][nc] == max_h:
                    continue
                
                needed = grid[nr][nc] - grid[r][c] + 1
                
        
                if needed <= remaining_k and (grid[nr][nc] - needed) >= 1:
                    orig_height = grid[nr][nc]
                    
                    grid[nr][nc] -= needed 
                    
                    dfs(nr, nc, remaining_k - needed, dist + 1)
                    
                    grid[nr][nc] = orig_height

    visited[r][c] = False

N, K = map(int, input().split())

grid = []
max_h = 0
for _ in range(N):
    row = list(map(int, input().split()))
    max_h = max(max_h, max(row))
    grid.append(row)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visited = [[False] * N for _ in range(N)]
answer = 0

starts = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == max_h:
            starts.append((r, c))

for sr, sc in starts:
    dfs(sr, sc, K, 1)

print(answer)
# bfs 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque
def is_range(r,c):
    return 0<= r < N and 0<= c < N 

def bfs(r,c):
    cnt = 1
    visited = [[False]*N for _ in range(N)]
    q = deque([(r,c)])
    visited[r][c]=True
    
    while q:
        cr, cc = q.popleft()
        
        for i in range(4):
            nx, ny = cr + dx[i], cc + dy[i]
            if is_range(nx,ny) and grid[nx][ny] == grid[cr][cc]+1 and not visited[nx][ny]:
                visited[nx][ny]=True   
                cnt += 1
                q.append((nx, ny))
                 
    return cnt       

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    max_len = 0
    min_node = int(1e9)
    res = ()
    for i in range(N):
        for j in range(N):
            is_start = True
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if is_range(ni,nj) and grid[ni][nj] == grid[i][j]-1:
                    is_start = False
                    break
            if not is_start:
                continue
            
            length = bfs(i,j)
            if length > max_len:
                max_len = length
                min_node = grid[i][j]
            elif length == max_len:
                if grid[i][j] < min_node:
                    min_node = grid[i][j]
    print(f'#{tc}',min_node, max_len)

    
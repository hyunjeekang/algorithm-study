dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque

def is_range(r,c): # 범위 확인 
    return 0<= r < N and 0<= c < M

def bfs(r,c): 
    q = deque([(r,c)])
    visited = [[False]*M for _ in range(N)]
    for_erase = []
    visited[r][c] = True
    
    while q: 
        cr, cc = q.popleft()
        
        for i in range(4):
            nx, ny = cr + dx[i], cc + dy[i]
            
            if is_range(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 0:
                    q.append((nx,ny))
                    
                elif grid[nx][ny] == 1:
                    for_erase.append((nx,ny))
    for x, y in for_erase:
        grid[x][y] = 0
    return len(for_erase)

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
t = 0
cheese = 0

while True:
    melted = bfs(0,0)
    
    if melted == 0:
        break
    
    cheese = melted
    t +=1
    
print(t)
print(cheese)

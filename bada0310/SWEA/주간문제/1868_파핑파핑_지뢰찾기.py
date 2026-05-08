# dirs= [(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(0,1),(1,0)]
#  0인곳을 먼저 bfs로 터트린다음 나머지 . 개수를 체크하면 됩니다
dr = [-1, 1, 0, 0, -1, -1, 1, 1]  
dc = [0, 0, -1, 1, -1, 1, -1, 1]

from collections import deque

def is_range(r,c):
    return 0<= r < N and 0<= c < N  #범위를 확인해주는 함수 

def star_count(r,c):
    star_cnt = 0
    for i in range(8):
        nr ,nc = r + dr[i], c + dc[i] # 8방향을 탐색하고 
        if is_range(nr,nc):
            if grid[nr][nc] == '*':
                star_cnt += 1  # 지뢰가 존재한다면 표시 
    return star_cnt # 그리고 8방향에 존재하는 지뢰의 갯수를 저장 

def show_cnt(r,c): # 회수를 세어주는 함수를 만들려고 했으나? 안됐다..? 반례의 경우 발생 
    q= deque([(r,c)])
    visited[r][c] = True
    # cnt = 0
    while q: 
        cr, cc = q.popleft()
        
        if cnt_grid[cr][cc] == 0:
            for i in range(8):
                nx ,ny = cr + dr[i], cc + dc[i]
                if is_range(nx,ny) and not visited[nx][ny]:
                    if grid[nx][ny] == '.': # and cnt_grid[nx][ny] == 0
                        visited[nx][ny] = True
                        q.append((nx,ny))
    # cnt += 1
    # return cnt

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    cnt_grid = [[0]*N for _ in range(N)] # 내 주변 8방향에 지뢰가 몇개 있는지 확인하는 그리드 
    visited = [[False]*N for _ in range(N)] #  bfs 탐색을 위한 방문 배열 
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                cnt_grid[i][j] = star_count(i,j) # 숫자넣는 그리드에 대입
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and not visited[i][j] and cnt_grid[i][j] == 0:
                show_cnt(i,j)
                cnt += 1
                
    for i in range(N): # 혼자 존재하는 . 이 있을수도 있다
        for j in range(N):
            if grid[i][j] == '.' and not visited[i][j]:
                cnt += 1
    print(f'#{tc}',cnt)
    
#dfs 도 가능하다 
# 연쇄 반응이라는게 결국에는 완전탐색이라서 
# 맵이 정해져있고 답이 정해져 있기 때문에 
# 0일때 dfs 호출을 반복한다 
# 내 기준으로 했을 때 너비 우선으로 하기 때문에 최단 경로라는게 나온다. 
# dfs 는 깊이 우선 탐색이기 때문에 최단 경로가 나오지 않을수도 있다.


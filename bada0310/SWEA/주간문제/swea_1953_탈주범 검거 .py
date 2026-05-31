# 요구사항 분석 
# 시간 T 에 따라서 멀어질 수 있는 거리가 달라진다 



from collections import deque
# 우 하 좌 상 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

pipe_dict = {
    1: [0,1,2,3],
    2: [1,3],
    3: [0,2],
    4: [0,3],
    5: [0,1],
    6: [1,2],
    7: [2,3]
}

def is_range(r,c):
    return 0<= r < N and 0<=c < M  and not visited[r][c] and grid[r][c] != 0

def move(r,c):
    q = deque([(r,c)])
    visited[r][c] = 1
    cnt =1 
    while q:
        cx, cy = q.popleft()
        if visited[cx][cy] >= L:
            continue
        curr_pipe = grid[cx][cy]
        
        for d in pipe_dict[curr_pipe]:
            nx = cx + dx[d]
            ny = cy + dy[d]
            if is_range(nx, ny):
                next_pipe = grid[nx][ny]
                
                opposite_d = (d+2)%4
                
                if opposite_d in pipe_dict[next_pipe]:
                    visited[nx][ny] = visited[cx][cy]+1
                    q.append((nx,ny))
                    cnt += 1
    return cnt 
    
T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)] # visited 배열 for bfs
    ans = move(R,C)
    print(f'#{tc} {ans}')
    
    
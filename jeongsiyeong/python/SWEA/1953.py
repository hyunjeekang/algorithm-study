from collections import deque

T = int(input())

pipes = {0:0, 1: 15, 2: 10, 3 : 5, 4:9, 5: 3, 6:6, 7:12}

dr = [ 0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r,c):
    return 0<=r<N and 0<=c<M

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [[False] * M for _ in range(N)]
    
    q = deque([(R, C, 1)])
    
    visited[R][C] = True
    
    answer = 1
    
    while q:
        cur_r, cur_c, time = q.popleft()
        if time == L:
            continue
        
        pipe = pipes[arr[cur_r][cur_c]]
        
        for i in range(4):
            if pipe & (1<<i):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                
                if is_range(nr,nc) and not visited[nr][nc]:
                    if pipes[arr[nr][nc]] & (1 << ((i+2)%4)):
                        answer+=1
                        visited[nr][nc] = True
                        q.append((nr,nc, time+1))
    print(f'#{test_case} {answer}')
                    
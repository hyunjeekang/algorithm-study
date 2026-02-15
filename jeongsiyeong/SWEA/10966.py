from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    q = deque()
    dist = [[-1] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                q.append((r,c))
                dist[r][c]=0
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    total_walk = 0

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0<=nr<N and 0<=nc<M and dist[nr][nc] == -1:
                dist[nr][nc] = dist[cur_r][cur_c] + 1
                q.append((nr,nc))

                total_walk += dist[nr][nc]
            
    print(f'#{test_case}', total_walk)



from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    return 0 <= r < N and 0 <= c < M

years = 0

while True:
    visited = [[False] * M for _ in range(N)]
    g_cnt = 0
    
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0 and not visited[r][c]:
                q = deque([(r, c)])
                visited[r][c] = True
                
                while q:
                    cur_r, cur_c = q.popleft()
                    for i in range(4):
                        nr = cur_r + dr[i]
                        nc = cur_c + dc[i]
                        
                        if is_range(nr, nc) and arr[nr][nc] > 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                g_cnt += 1

    if g_cnt >= 2:
        print(years)
        break
    if g_cnt == 0:
        print(0)
        break

    melt_list = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                sea_count = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if is_range(nr, nc) and arr[nr][nc] == 0:
                        sea_count += 1
                
                if sea_count > 0:
                    melt_list.append((r, c, sea_count))

    for r, c, melt_amount in melt_list:
        arr[r][c] = max(0, arr[r][c] - melt_amount)

    years += 1
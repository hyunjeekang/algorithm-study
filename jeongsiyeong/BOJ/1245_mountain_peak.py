from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def is_range(r,c ):
    return 0<=r<N and 0<=c<M

dr = [0, 1, 0, -1, 1,1, -1, -1]
dc = [1, 0, -1, 0, 1, -1,1, -1]

visited = [[False] *M for _ in range(N)]

peak_cnt = 0

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            q = deque([(r,c)])
            
            is_peak = True
            
            while q:
                cur_r, cur_c = q.popleft()
                
                for i in range(8):
                    nr = cur_r + dr[i]
                    nc = cur_c + dc[i]
                    if is_range(nr,nc) :
                        if arr[nr][nc] > arr[cur_r][cur_c]:
                            is_peak = False
                        elif arr[nr][nc] == arr[cur_r][cur_c] and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr,nc))
            if is_peak:
                peak_cnt += 1
                            
print(peak_cnt)            
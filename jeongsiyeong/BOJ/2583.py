from collections import deque

def is_range(r,c,max_r,max_c):
    return r>=0 and r<max_r and c>=0 and c<max_c

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


N, M, K = map(int, input().split())

field = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
    
for _ in range(K):
    a_c, a_r, b_c, b_r = map(int, input().split())
    
    for r in range(a_r, b_r):
        for c in range(a_c, b_c):
            field[r][c] = 1
areas = []
worm_count = 0
for r in range(N):
    for c in range(M):
        if not visited[r][c] and field[r][c] == 0:
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            area_count=1
            while q:
                cur_r, cur_c = q.popleft()
                    

                for dir in range(4):
                    nr = cur_r + dr[dir]
                    nc = cur_c + dc[dir]

                    if is_range(nr, nc, N, M):
                        if not visited[nr][nc] and field[nr][nc] == 0:
                            visited[nr][nc] = True
                            area_count+=1
                            q.append((nr, nc))
            worm_count+=1
            areas.append(area_count)
print(worm_count)
areas.sort()
print(*areas)
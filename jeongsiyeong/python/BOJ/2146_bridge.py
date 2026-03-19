from collections import deque
N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
island_id = 1
lands = {}

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r,c):
    return 0<=r<N and 0<=c<N

def bfs_labeling(r, c, island_id):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    map[r][c] = island_id
    lands.setdefault(island_id, [(r,c)])

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if is_range(nr,nc) and not visited[nr][nc] and map[nr][nc] == 1:
                map[nr][nc] = island_id
                visited[nr][nc] = True
                q.append((nr, nc))
                lands[island_id].append((nr,nc))
        
for r in range(N):
    for c in range(N):
        if map[r][c] == 1 and not visited[r][c]:
            bfs_labeling(r, c, island_id)
            island_id+=1

def bfs_shortest_path(island_n):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for land_r, land_c in lands[island_n]:
        q.append((land_r, land_c))
        dist[land_r][land_c] = 0

    while q:
        cur_r, cur_c = q.popleft()

        if dist[cur_r][cur_c] >= ans:
            continue
        
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if is_range(nr, nc):
                if map[nr][nc] != 0 and map[nr][nc] != island_n:
                    return dist[cur_r][cur_c]
                
                if map[nr][nc] == 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[cur_r][cur_c] + 1
                    q.append((nr,nc))
    return float('inf')

ans = float('inf')

for i in range(1, island_id):
    result = bfs_shortest_path(i)
    ans = min(ans, result)

print(ans)
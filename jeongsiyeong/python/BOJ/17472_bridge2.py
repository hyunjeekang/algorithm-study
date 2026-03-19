from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r,c):
    return 0<=r<N and 0<=c<M

def set_comp_num():
    visited = [[False] * M for _ in range(N)]
    num = 1
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 0 and not visited[r][c]:
                q = deque()
                q.append((r,c))
                arr[r][c] = num
                visited[r][c] = True
                
                while q:
                    cur_r, cur_c = q.popleft()
                    for i in range(4):
                        nr = cur_r + dr[i]
                        nc = cur_c + dc[i]
                        if is_range(nr, nc) and not visited[nr][nc]:
                            if arr[nr][nc] != 0:
                                visited[nr][nc] = True
                                arr[nr][nc] = num
                                q.append((nr,nc))
                num += 1
    return num

def find_bridges():
    b_list = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 0:
                cur_island = arr[r][c]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    
                    b_cnt = 0
                    
                    while is_range(nr,nc) and arr[nr][nc] == 0:
                        nr += dr[i]
                        nc += dc[i]
                        b_cnt += 1
                    if is_range(nr,nc) and arr[nr][nc] != cur_island:
                        if b_cnt >= 2:
                            b_list.append((b_cnt, cur_island, arr[nr][nc]))
    return b_list

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b            

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]  

num = set_comp_num()    

parent = [i for i in range(num)]

b_list = find_bridges()
b_list.sort()

total_dist = 0
connected_edges = 0

for dist, island_a, island_b in b_list:
    if find(island_a) != find(island_b):
        union(island_a, island_b)
        total_dist += dist
        connected_edges += 1

if connected_edges == (num -2):
    print(total_dist)
else:
    print(-1)
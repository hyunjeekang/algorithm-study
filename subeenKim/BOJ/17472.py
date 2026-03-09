from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# bfs로 모든 섬 찾아서 섬 번호 붙이기
visited = [[False]*M for _ in range(N)]
num = 0 # 섬 번호
for x in range(N):
    for y in range(M):
        if not visited[x][y] and grid[x][y] == 1:
            num += 1
            q = deque([(x, y)])
            visited[x][y] = True
            grid[x][y] = num

            while q :
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        grid[nr][nc] = num
                        q.append((nr, nc))

# 섬과 섬 사이의 다리 길이 구하기 (num -> 섬 개수)
bridge_length = [[float('inf')]*num for _ in range(num)]

for x in range(N):
    for y in range(M):
        if grid[x][y] > 0 : # 섬일 때
            i1 = grid[x][y]
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                mx, my = x+dr, y+dc
                while 0 <= mx < N and 0 <= my < M and grid[mx][my] == 0:
                    mx, my = mx+dr, my+dc
                if 0 <= mx < N and 0 <= my < M :
                    if grid[mx][my] != i1:
                        diff = abs(x-mx)+abs(y-my) - 1
                        if 2 <= diff < bridge_length[i1-1][grid[mx][my]-1]:
                            bridge_length[i1-1][grid[mx][my]-1] = diff

# 섬에 다리 놓기 (Prim 알고리즘)
def prim():
    visit_set = set()
    visit_set.add(0)
    dist = 0
    for _ in range(num-1): # 다리의 수는 섬의 수 - 1
        min_dist, next_i = float('inf'), -1
        for i in visit_set:
            for j in range(num):
                if j not in visit_set and 0 < bridge_length[i][j] < min_dist:
                    next_i = j
                    min_dist = bridge_length[i][j]
        if min_dist == float('inf'):
            return -1
        visit_set.add(next_i)
        dist += min_dist
    return dist

print(prim())
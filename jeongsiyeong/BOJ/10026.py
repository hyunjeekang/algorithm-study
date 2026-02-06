from collections import deque
n = int(input())

arr = [list(input()) for _ in range(n)]

n_count = 0
m_count = 0

r_count = 0
g_count = 0
b_count = 0
rg_count = 0
visited = [[False]*n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    return 0<=r<n and 0<=c<n
def refresh():
    global visited
    visited = [[False]*n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if not visited[r][c] and arr[r][c] == 'R':
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            while q:
                cur_r, cur_c = q.popleft()
                
                for dir in range(4):
                    nr = cur_r + dr[dir]
                    nc = cur_c + dc[dir]
                    if is_range(nr, nc):
                        if not visited[nr][nc] and arr[nr][nc] == 'R':
                            visited[nr][nc] = True
                            q.append((nr, nc))
            r_count+=1
            refresh()
        elif not visited[r][c] and arr[r][c] == 'B':
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            while q:
                cur_r, cur_c = q.popleft()
                
                for dir in range(4):
                    nr = cur_r + dr[dir]
                    nc = cur_c + dc[dir]
                    if is_range(nr, nc):
                        if not visited[nr][nc] and arr[nr][nc] == 'B':
                            visited[nr][nc] = True
                            q.append((nr, nc))
            b_count+=1
            refresh()
        elif not visited[r][c] and arr[r][c] == 'G':
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            while q:
                cur_r, cur_c = q.popleft()
                
                for dir in range(4):
                    nr = cur_r + dr[dir]
                    nc = cur_c + dc[dir]
                    if is_range(nr, nc):
                        if not visited[nr][nc] and arr[nr][nc] == 'G':
                            visited[nr][nc] = True
                            q.append((nr, nc))
            g_count+=1
            refresh()
        if not visited[r][c] and (arr[r][c] == 'G' or arr[r][c] == 'R') :
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            while q:
                cur_r, cur_c = q.popleft()
                
                for dir in range(4):
                    nr = cur_r + dr[dir]
                    nc = cur_c + dc[dir]
                    if is_range(nr, nc):
                        if not visited[nr][nc] and (arr[r][c] == 'G' or arr[r][c] == 'R'):
                            visited[nr][nc] = True
                            q.append((nr, nc))
            rg_count+=1
            refresh()    
n_count = r_count + g_count + b_count
m_count = b_count + rg_count    
print(n_count, m_count)

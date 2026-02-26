from collections import deque
N, M = map(int,input().split())
maze = [list(input()) for _ in range(N)]

def is_range(r,c):
    return 0<=r<N and 0<=c<M

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

start_r, start_c = 0, 0
for r in range(N):
    for c in range(M):
        if maze[r][c] == '0':
            start_r, start_c = r, c
            maze[r][c] = '.'
q = deque([(start_r,start_c, 0 , 0)])
visited = [[[False] * 64 for _ in range(M)] for _ in range(N)]
visited[start_r][start_c][0] = True
while q:
    cur_r, cur_c, cur_cnt, cur_key = q.popleft() 
    if maze[cur_r][cur_c] == '1':
        print(cur_cnt)
        exit(0)

    for i in range(4):
        nr = cur_r+dr[i]
        nc = cur_c+dc[i]
        if is_range(nr, nc) and maze[nr][nc] != '#' :
            cell = maze[nr][nc]
            if cell == '.' or cell == '1':
                if not visited[nr][nc][cur_key]:
                    q.append((nr,nc,cur_cnt+1, cur_key))
                    visited[nr][nc][cur_key] = True
            elif 'A' <= cell <= 'F':
                if not visited[nr][nc][cur_key]:
                    if cur_key & (1<<(ord(cell) - ord('A'))) :
                        q.append((nr,nc,cur_cnt+1,cur_key))
                        visited[nr][nc][cur_key] = True
            elif 'a'<=cell<='f':
                nxt_key = cur_key | (1<<(ord(cell) - ord('a')))
                if not visited[nr][nc][nxt_key]:
                    q.append((nr,nc,cur_cnt+1, nxt_key))
                    visited[nr][nc][nxt_key] = True
print(-1)

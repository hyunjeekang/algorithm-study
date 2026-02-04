#백준 1012 유기농 배추
from collections import deque

#좌표가 범위내에 있는지 확인
def is_range(r,c,max_r,max_c):
    return r>=0 and r<max_r and c>=0 and c<max_c

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

t = int(input())

for _ in range(t):
    M,N,K = map(int, input().split())

    field = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1

    worm_count = 0
    for r in range(N):
        for c in range(M):
            # 아직 조회 안한 배추면
            if not visited[r][c] and field[r][c] == 1:
                #bfs
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                while q:
                    cur_r, cur_c = q.popleft()
                    
                    for dir in range(4):
                        nr = cur_r + dr[dir]
                        nc = cur_c + dc[dir]
                        #주변에 조회 안한 배추가 있으면 큐에 집어넣기
                        if is_range(nr, nc, N, M):
                            if not visited[nr][nc] and field[nr][nc] == 1:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                worm_count+=1
    print(worm_count)
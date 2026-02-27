from collections import deque
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def is_range(r,c):
    return 0<=r<N and 0<=c<M

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_melted():
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                return False
    return True

def set_cheese():
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                arr[r][c] = 1

cnt = 0

while not is_melted():
    q = deque()
    visited = [[False] * M for _ in range(N)]

    r, c = 0, 0
    q.append((r,c))
    visited[r][c] = True
    while q:
        cur_r, cur_c= q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if is_range(nr, nc) and not visited[nr][nc]:
                if arr[nr][nc] > 0:
                    arr[nr][nc]  = arr[nr][nc] + 1
                    if arr[nr][nc] >= 3:
                        arr[nr][nc] = 0
                        visited[nr][nc] = True
                else:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    cnt+=1
    set_cheese()

print(cnt)

                
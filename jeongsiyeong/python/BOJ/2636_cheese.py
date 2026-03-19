from collections import deque
N, M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    q = deque([(0,0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    cnt = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c+dc[i]

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                if arr[nr][nc]==0:
                    visited[nr][nc] = True
                    q.append((nr,nc))
                elif arr[nr][nc] == 1:
                    visited[nr][nc] = True
                    arr[nr][nc] = 0
                    cnt += 1
    return cnt

time = 0
last_cheese = 0

while True:
    melted_cnt = bfs()
    if melted_cnt == 0:
        break

    last_cheese = melted_cnt
    time +=1

print(time)
print(last_cheese)
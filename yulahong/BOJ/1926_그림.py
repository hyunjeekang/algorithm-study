from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    size = 0

    while q:
        cr, cc = q.popleft()
        size += 1

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if  0 <= nr < n and  0 <= nc < m:
                if map[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr, nc])

    return size

cnt = 0 # 전체 그림 개수
max_paintings = 0 # 그림의 최댓값

for i in range(n): # 세로
    for j in range(m): # 가로
        if map[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            #전체 그림 개수 +1
            cnt +=1
            # bfs > 그림 크기를 구하고 최댓값 갱신
            max_paintings = max(max_paintings, bfs(i, j))

print(cnt)
print(max_paintings)
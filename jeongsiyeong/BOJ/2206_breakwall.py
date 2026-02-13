from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

q = deque()
q.append((0, 0, 0))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solve():
    while q:
        cur_r, cur_c, broken = q.popleft()

        if cur_r == N - 1 and cur_c == M - 1:
            return visited[cur_r][cur_c][broken]

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and broken == 0:
                    visited[nr][nc][1] = visited[cur_r][cur_c][0] + 1
                    q.append((nr, nc, 1))
                
                elif arr[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                    visited[nr][nc][broken] = visited[cur_r][cur_c][broken] + 1
                    q.append((nr, nc, broken))
    
    return -1

print(solve())
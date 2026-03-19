from collections import deque
import sys
input = sys.stdin.readline
#보물섬
H, W = map(int, input().split())

maps = [input() for _ in range(H)]

def is_range(r,c):
    return 0<=r<H and 0<=c<W

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

mx_dist=0
for r in range(H):
    for c in range(W):
        if maps[r][c] == 'L':
            visited = [[False for _ in range(W)] for _ in range(H)]
            q = deque()
            q.append((r,c,0))
            visited[r][c] = True
            while q:
                rr, cc, dist = q.popleft()
                for direction in range(4):
                    nc = cc + dc[direction]
                    nr = rr + dr[direction]
                    if is_range(nr, nc) and not visited[nr][nc] and maps[nr][nc] == 'L':
                        is_open = True
                        q.append((nr, nc, dist+1))
                        visited[nr][nc] = True
            mx_dist = max(mx_dist, dist)

print(mx_dist)

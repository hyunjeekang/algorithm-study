#백준 10711번 모래성
from collections import deque
H, W = map(int, input().split())

sands = [list(input()) for _ in range(H)]

dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]

def is_range(r,c):
    return 0<=r<H and 0<=c<W

cnt = 0
q = deque()
for r in range(H):
    for c in range(W):
        if sands[r][c] == '.':
            q.append((r,c))
        else:
            sands[r][c] = int(sands[r][c])
cnt=0
while q:
    for _ in range(len(q)):
        cur_r, cur_c = q.popleft()

        for i in range(8):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if is_range(nr,nc) and sands[nr][nc] != '.':
                sands[nr][nc] -= 1
                if sands[nr][nc] == 0:
                    sands[nr][nc] = '.'
                    q.append((nr,nc)) 
    if q:
        cnt+=1
print(cnt)
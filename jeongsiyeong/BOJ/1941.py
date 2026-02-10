from collections import deque
#소문난 칠공주

girls = [input() for _ in range(5)]

count = 0

def is_range(r,c):
    return 0<=r<5 and 0<=c<5

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(5):
    for c in range(5):
        visited =[ [False]*5 for _ in range(5)]
        q = deque()
        if girls[r][c] == 'S':
            q.append((r, c, 1, 0))
        else:
            q.append((r,c,0,1))
        
        while q:
            curr_r, curr_c, s_cnt, d_cnt = q.popleft()

            if s_cnt + d_cnt == 7:
                if s_cnt >= 4:
                    count+=1
                break
            for dir in range(4):
                nr = curr_r + dr[dir]
                nc = curr_c + dc[dir]
                if is_range(nr,nc):
                    if girls[nr][nc] == 'S':
                        q.append((nr, nc, s_cnt+1, d_cnt))
                    else:
                        q.append((nr, nc, s_cnt, d_cnt+1))
print(count) 



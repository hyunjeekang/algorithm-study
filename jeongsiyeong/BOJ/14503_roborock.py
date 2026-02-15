#로보락 문제
N, M = map(int, input().split())

robo_r, robo_c, dir = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
#북 동 남 서
#반시계 == -1

def is_range(r,c):
    return 0<=r<N and 0<=c<M

cleaned = 0
while True:
    if arr[robo_r][robo_c] == 0:
        arr[robo_r][robo_c] = 2
        cleaned += 1
    is_dust = False
    for i in range(4):
        nr = robo_r + dr[i]
        nc = robo_c + dc[i]
        if is_range(nr,nc) and arr[nr][nc] == 0:
            is_dust = True
            break
    if not is_dust:
        nr = robo_r - dr[dir]
        nc = robo_c - dc[dir]
        if is_range(nr, nc) and arr[nr][nc] != 1:
            robo_r = nr
            robo_c = nc
            continue
        elif is_range(nr,nc) and arr[nr][nc] == 1:
            break
    else:
        dir = (dir - 1) % 4
        nr = robo_r + dr[dir]
        nc = robo_c + dc[dir]
        if is_range(nr, nc) and arr[nr][nc] == 0:
            robo_r = nr
            robo_c = nc
            continue
print(cleaned)
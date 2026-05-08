N, M = map(int, input().split())

cur_r, cur_c, cur_d = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0

while True:
    if grid[cur_r][cur_c] == 0:
        answer += 1
        grid[cur_r][cur_c] = 2
        
    is_washable = False
    
    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        
        if 0<=nr<N and 0<=nc<M:
            if grid[nr][nc] == 0:
                is_washable = True
                break
            
    if not is_washable:
        nr = cur_r - dr[cur_d]
        nc = cur_c - dc[cur_d]
        if 0<=nr<N and 0<=nc<M:
            if grid[nr][nc] != 1:
                cur_r = nr
                cur_c = nc
                continue
            elif grid[nr][nc] == 1:
                break
    else:
        cur_d = (cur_d - 1) % 4
        nr = cur_r + dr[cur_d]
        nc = cur_c + dc[cur_d]
        if 0<=nr<N and 0<=nc<M and grid[nr][nc] == 0:
            cur_r = nr
            cur_c = nc
            continue
 
print(answer)
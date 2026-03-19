def dfs(depth, cnt, current_len):
    global max_cnt, min_len
    
    if cnt + (len(cores) - depth) < max_cnt:
        return

    if depth == len(cores):
        if cnt > max_cnt:
            max_cnt = cnt
            min_len = current_len
        elif cnt == max_cnt:
            min_len = min(min_len, current_len)
        return
    
    x, y = cores[depth]
    
    for d in range(4):
        nx, ny = x, y
        length = 0
        can_connect = True
        
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 0: 
                    can_connect = False
                    break
                length += 1
            else:
                break 
                
        if can_connect:
            nx, ny = x, y
            for _ in range(length):
                nx += dx[d]
                ny += dy[d]
                graph[nx][ny] = 2
                
            dfs(depth + 1, cnt + 1, current_len + length)
            
            nx, ny = x, y
            for _ in range(length):
                nx += dx[d]
                ny += dy[d]
                graph[nx][ny] = 0

    dfs(depth + 1, cnt, current_len)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    cores = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    continue
                cores.append((i, j))
    
    max_cnt = 0
    min_len = float('inf')
    
    dfs(0, 0, 0)
    
    print(f"#{tc} {min_len}")
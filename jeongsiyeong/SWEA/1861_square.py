T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(cur_r, cur_c, start, depth):
    global answer, room_n
    
    is_way = False
    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] - arr[cur_r][cur_c] == 1:
                is_way = True
                dfs(nr, nc, start, depth + 1)
                
    if not is_way:
        if depth > answer:
            answer = depth
            room_n = start
        elif depth == answer:
            room_n = min(room_n, start)

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    answer = 0
    room_n = float('inf') 
    
    for r in range(N):
        for c in range(N):
            dfs(r, c, arr[r][c], 1)
            
    print(f'#{test_case} {room_n} {answer}')
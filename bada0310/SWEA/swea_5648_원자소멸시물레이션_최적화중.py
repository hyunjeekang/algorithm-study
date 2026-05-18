dx = [0, 0, -1, 1] # 상 하 좌 우 
dy = [1, -1, 0, 0]

# 범위내에 존재하는지 확인 
# def is_range(r, c):
#     return -2000 <= r <= 2000 and -2000 <= c <= 2000
def move(arr):
    new_pos = {}
    
    for x, y, dir, cost in arr:   
        nx, ny = x + dx[dir], y + dy[dir]  # 한 방향으로만 이동 
        if not (-2000 <= nx <= 2000 and -2000 <= ny <= 2000): # if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
            continue # 범위를 벗어난 경우 
        
        if (nx,ny) in new_pos:
            new_pos[(nx,ny)].append((dir,cost))
        else:
            new_pos[(nx,ny)] = [(dir,cost)]
                   
    new_micro = []
    total_num = 0
    for (x,y), group in new_pos.items(): # (x,y)=key, group=val
        if len(group) == 1:
            new_micro.append((x,y,group[0][0], group[0][1]))
        else:
            for dir, cost in group:
                total_num += cost
    return new_micro, total_num

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    
    for _ in range(N):
        x, y, dir, cost = map(int,input().split())
        arr.append((x*2 , y*2 , dir, cost))
    
    total_answer = 0
    
    while arr:
        arr, total_num = move(arr)
        total_answer += total_num
    print(f'#{tc} {total_answer}')
# [조건 범위]
# 1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)
# 2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)
# 3. 원자들의 처음 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)


# [요구사항 정리]
# # 이동속도는 동일하다 t=1 
# 미생물 문제와 유사 
# 상하 좌우  순서로 dx dy  구성 필요 
# 최초위치에서 동시에 이동을 시작 
# 마주치면 방출 에너지에 저장 
# 바라보는 방향도 계산해주어야 함  # 상(0), 하(1), 좌(2), 우(3)

# [풀이방법]
# nx,ny 가  0>= or N-1 >= 이 되면 삭제 하는 방식으로 구현
# 

# continue 와 return 에 대해 다시생각해볼 필요 

# 상핮좌우 순 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 범위내에 존재하는지 확인 
def is_range(r, c):
    return -2000 <= r <= 2000 and -2000 <= c <= 2000

def move(arr):
    new_pos = {} # dict 
    
    for x, y, dir, cost in arr:
        if dir == 0:
            nx, ny = x + dx[0], y + dy[0]
        elif dir == 1:
            nx, ny = x + dx[1], y + dy[1]
        elif dir == 2: 
            nx, ny = x + dx[2], y + dy[2]
        elif dir == 3: 
            nx, ny = x + dx[3], y + dy[3]
            
        # nx, ny = x + dx[dir], y + dy[dir]  # 한 방향으로만 이동 
        if not is_range(nx,ny): # if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
            continue # 범위를 벗어난 경우 
        
        if (nx,ny) not in new_pos:
            new_pos[(nx,ny)] = []
        new_pos[(nx,ny)].append((dir,cost))
                   
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
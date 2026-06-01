# # # 터널끼리 연결이 되어 있는 경우 이동이 가능
# 탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며 
# 탈주범이 있을 수 있는 위ㅣ의 개수 계산하기 
# 탈주범은 시간당 1의 거리를 움직일 수 있음 
######탈주범이 있을 수 있는 위치의 개수를 계산하여야함#####


####### 터널 구조물간의 연결성이 중요 ########
##### 파이프가 뚫려있나? == 다음칸의 파이프 == 나를 향해 있어야함 #####
#####  상-하, 좌-우 #####
# 숫자 1-7 : 해당 위치의 터널 구조물 타입 
# 숫자 0 : 터널이 없는 장소 

# 상 하 좌 우 
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 상-하, 하-상,좌-우, 우-좌 
opp = {0:1, 1:0, 2:3, 3:2}

# 터널 뚫린곳 
tunnel = {
    1:[0,1,2,3],
    2:[0,1],
    3:[2,3],
    4:[0,3],
    5:[1,3],
    6:[1,2],
    7:[0,2]
}

def bfs(sx,sy,L):
    # 위치,L 표시 
    queue = [(sx,sy,1)] # 시간당 1의 거리,,,,,,, 이미 움직아곳 넣으니까 1인듯 
    visited= [[False]*M for _ in range(N)]

    visited[sx][sy] = True

    count = 1 # 탈주범이 위치할 수 있는 곳의 개수 

    while queue:
        x,y,t = queue.pop(0)

        # L시간에 도달헀다면 다음 칸으로 확장 ㄴㄴ
        if t== L:
            continue

        cur_tunnel = grid[x][y]

        for d in tunnel[cur_tunnel]:
            nr = x + dr[d]
            nc = y + dc[d]

            # 경계췍 + 방문췍 + 빈 공간 아닌지 췍 
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] >0:
                if not visited[nr][nc]:
                    next_tunnel = grid[nr][nc]

                # 다음 터널이 열려있는지 검사 
                # d 방향으로 가니까, 다음 터널에는 opp[d] 방행이 포함되어 있어야함 

                    if opp[d] in tunnel[next_tunnel]:

                        if t + 1 <= L:
                            visited[nr][nc] = True
                            count += 1
                            queue.append((nr,nc,t+1))

    return count 


T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int(input().split()))
    # 세로크기 N, 가로크기 M, 맨홀 뚜껑 위치 세로 R, 맨홀 뚜껑 위치 가로 C , 탈출 후 소요 시간 L

    # 지도 입력 받기 
    grid = []
    for _ in range(N):
        grid.append(list(map(int(input().split()))))

        result = bfs(R,C,L)

    print(f'#{tc} {result}')


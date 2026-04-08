
from collections import deque
# 16*16 행렬의 미로 . 흰색=길, 노랑 = 벽
# (0,0) == 기준으로 , 가로방향 = x방향 , 세로방향 = y방향 ,
# 미로의 시작점 = (1,1) 도착점 = (13,13)

# 1 = 벽, 0 = 길, 2 = 출발점, 3=도착점
dr = [0,0,-1,1] # 상하좌우
dc = [-1,1,0,0]
T = 10
for tc in range(1,T+1):
    test = int(input())

    arr = [list(map(int,input())) for _ in range(16)]
    visited =[[False]*16 for _ in range(16)] # 방문배열


    for r in range(16):
        for c in range(16):
            if arr[r][c] == 2:
                sr,sc = r,c # 시작점으로 만들기
                visited[sr][sc] = True

    q = deque()
    cnt = 0
    q.append((sr, sc))
    find = False
    while q:
        cur_r,cur_c = q.popleft() #현재점으로 설정

        # 종료조건
        if arr[cur_r][cur_c] == 3: # 3을 만나면
            find = True
            print(f'#{test} 1')
            break



        for i in range(4): # 4방향으로 진행할게
            nr = cur_r + dr[i] # 주변 좌표 정해줄게
            nc = cur_c + dc[i]

            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc]:
                if arr[nr][nc] != 1: # 3을 가긴 해야하니까 1이 아니라면으로
                    q.append((nr,nc)) # 주변값 들어가게 해
                    visited[nr][nc] = True # 방문처리했고

    if find == False:
        print(f"#{test} 0")










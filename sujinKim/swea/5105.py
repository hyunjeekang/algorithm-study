from collections import deque

dr = [0,0,-1,1] # 상하좌우
dc = [-1,1,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input()))for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # 0 == 통로
    # 1 == 벽
    # 2 == 출발
    # 3 == 도착
    # 최소 몇 개의 칸을 지나야 출발지에서 도착지에 다다를 수 있는지
    # 지나야하는 최소한의 칸 수 / 경로가 없는 경우 0
    for r in range(N): # 행의 수
        for c in range(N): # 열의 수
            if arr[r][c] == 2: # 출발지 찾으면
                sr,sc = r,c # 출발지 할당
                visited[sr][sc] = True

    cnt = 0
    q = deque() # 좌표 넣는곳
    q.append((cnt,sr,sc))
    find = False
    while q:
        cur_cnt,cur_r, cur_c = q.popleft() # q에서 나와서 현재값으로 하기


        # 종료조건
        if arr[cur_r][cur_c] == 3:
            find =True
            print(f'#{tc} {cur_cnt-1}')
            break




        for i in range(4): # 4방향으로 가는데 , 1칸씩 이동
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]   # 방향으로 가는거

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]: # 경계췍



                if arr[nr][nc] != 1: # 0이라면 이동 가능
                    q.append((cur_cnt+1,nr,nc))
                    visited[nr][nc] = True

    if find == False:

        print(f"#{tc} 0")

T = int(input())
 
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
 
### 풀이 1 : 가로와 세로를 따로 탐색하는 방법
    # 가로 탐색
    x, y = 0, 0
    while x < N:
        cnt = 0
        while y < N:
            if puzzle[x][y] == 1 :
                cnt += 1
            else :
                if cnt == K :
                    answer += 1
                cnt = 0
            y += 1
        if cnt == K : # y 좌표가 N-1 까지 갔을 때 cnt 값 확인
            answer += 1    
        x, y = x+1, 0
 
    # 세로 탐색
    x, y = 0, 0
    while y < N:
        cnt = 0
        while x < N:
            if puzzle[x][y] == 1 :
                cnt += 1
            else :
                if cnt == K :
                    answer += 1
                cnt = 0
            x += 1
        if cnt == K : # x 좌표가 N-1 까지 갔을 때 cnt 값 확인
            answer += 1    
        x, y = 0, y+1
 
### 풀이 2 : 가로와 세로를 한 번에 확인하는 방법
    # dx = [1, 0] # right under
    # dy = [0, 1]
 
    # for x in range(N) :
    #     for y in range(N):
    #         if puzzle[x][y] == 1 :
    #             for d in range(2):
    #                 nx, ny = x, y
    #                 # 연속된 빈칸이 있을 때, 한 번 센건 세지 않기 위함 (첫번째로 빈칸이 나왔을 때만 셈)
    #                 if (0 <= nx-dx[d] and 0 <= ny-dy[d]) and (puzzle[nx-dx[d]][ny-dy[d]] == 1) :
    #                     continue
    #                 cnt = 1
    #                 while 0 <= nx+dx[d] < N and 0 <= ny+dy[d] < N : # x와 y의 범위가 N*N 배열 안에 있을 때
    #                     if puzzle[nx+dx[d]][ny+dy[d]] == 1 : # 하얀 칸이면 cnt 하나 늘리고, nx, ny를 다음 칸으로 이동해 계속 하얀 칸 찾기
    #                         cnt += 1
    #                         nx, ny = nx+dx[d], ny+dy[d]
    #                     else :
    #                         break
    #                 if cnt == K : # 연속된 하얀 칸의 길이가 K와 같으면
    #                     answer += 1
 
    print(f'#{test_case} {answer}')
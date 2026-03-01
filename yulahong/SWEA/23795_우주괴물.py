# N인 이차원 그리드
# 괴물은 상하좌우 광선
# 벽에 막히면 멈춤
# 델타로 탐색

T = int(input()) #테케수
    # 상좌우하
dr = [-1, 0, 1, 0] 
dc = [0, 1, 0, -1]

for tc in range(1, T+1):

    N = int(input()) 
    arr = [ list(map(int, input().split())) for _ in range(N)] #이차원 그리드

    # 지도탐색
    # 0 = 빈칸, 1 = 벽, 2 = 괴물
    # 괴물 좌표 찾고
    # 0이면 1로 바꾸기
    # 1 만나면 그만하기

    for cr in range(N):
        for cc in range(N):
            if arr[cr][cc] == 2:

                for dir in range(4): #광선 발사
                    nr = cr + dr[dir]
                    nc = cc + dr[dir]

                    while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1: #경계선 검사: 범위 안에 있거나 벽이 아닐 때
                        if arr[nr][nc] == 0: #광선 발사해서 만약 빈칸이면
                            arr[nr][nc] == 1 #벽으로 바꿔줌

                        nr += dr[dir]
                        nc += dc[dir]

            
    # 광선 발사가 끝나고 0 개수 세기
    count_zero = 0  # 0의 개수를 새로운 테스트케이스마다 초기화 해야함
    for row in area:
        for cell in row:
            if cell == 0:
                count_zero += 1
                 
                 
    print(f'#{tc} {count_zero}')







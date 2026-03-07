# N*N 그리드
# 각 칸에는 돌 있거나 없음
# 돌이 가로 세로 대각선 오목 찾기
# 정답 형식 : YES or NO 

# 변수
T = int(input())
dr = [-1, -1, -1, 0, 0, 1, 1, 1] 
dc = [-1, 0, 1, 1, -1, 1, 0, -1]
# 행순회 열순회 해서 o 찾기
# 찾으면 8 방향 델타 탐색 시작
#  dr = [-1, -1, -1, 0, 0, 1, 1, 1] #상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
#  dc = [-1, 0, 1, 1, -1, 1, 0, -1]
# 범위 안에 들어오고 길이가 5 찾으면 바로 yes 출력 > 초기값 no로 두기
# 길이가 5 어떻게 찾을거임?> 쉽지 않네 

for tc in range(1, T+1):

    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'NO'

    for cr in range(N):
        for cc in range(N):
            if arr[cr][cc] == 'o':

                for dir in range(8):
                    nr = cr + dr[dir]
                    nc = cc + dc[dir]
                    cnt = 1

                    # if ans == 'YES': 민식오빠의 더 효율적인 코드를 위한 팁!
                    #     break


                    while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        cnt += 1
                        nr += dr[dir]
                        nc += dc[dir]
                        if cnt == 5:
                            ans = 'YES'
                            break

    print(f'#{tc} {ans}')
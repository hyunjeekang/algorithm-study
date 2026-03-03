# 문제 설명
# 토마토 N*M 상자에 보관
# 만약 시간이 아무리 지나도 토마토가 모두 익을 수 없으면 -1 출력
# 하루 지나면 익은 토마토 인접 토마토 익음 > 상하좌우
# 최소 일수 > BFS?

# 변수
# 1번줄: 가로 = M, 세로 = N
# 그 다음 줄 토마토 정보> 1 = 익은 토마토, 0 = 익지 않은 토마토 -1 = 빈칸

# 덱 만들기
# M*N 그리드 만들기
# 1인 토마토 위치 찾아서 시작하기
# 델타로 탐색해서 0 이면 1로 바꾸기
# visited 배열 만들어서 중복 방지?
# COUNT = 0 만들어서 최소 날짜 저장

from collections import deque
import sys

dr = [-1, 0, 1, 0]
dc = [0, 1, 0 ,-1]

M, N = map(int, input().split())

box_arr = [list(map(int, input().split())) for _ in range(N)]
visited_arr = [[-1] * M for _ in range(N)] # 날짜 누적할 거임 익은 사과 찾으면 0할당해서 계속 +1하는 방식

q = deque()

for i in range(N): #가로 세로 헷갈리지 말기
    for j in range(M):
        if box_arr[i][j] == 1: # 익은 사과 발견하면
            q.append(( i, j )) #빈 덱에 저장
            visited_arr[i][j] = 0 # -1인 방문배열 좌표 0으로 바꿔주기


while q:
    cr, cc = q.popleft()
            
    for dir in range(4): #찾은 후에 현재 좌표에서 델타 탐색
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        #조건:범위 박스에 0이고, 방문 배열이 -1이고
        if 0 <= nr < N and 0 <= nc <M:
            if box_arr[nr][nc] == 0 and visited_arr[nr][nc] == -1:
                visited_arr[nr][nc] = visited_arr[cr][cc] + 1
                q.append((nr, nc))

cnt = [] #값 저장할 새로운 리스트 할당
for a in range(N):
    for b in range(M):

        if visited_arr[a][b] == -1 and box_arr[a][b] == 0: #만약 익지않은 토마토가 있다면
            print(-1) #-1 출력하고
            exit() #탈출!!

        cnt.append(visited_arr[a][b]) #visited_arr의 값들 저장하기

ans = max(cnt) #그 중 가장 큰 값이 우리가 원하는 정답

print(ans)
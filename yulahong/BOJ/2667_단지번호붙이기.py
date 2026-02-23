# # 지도의 크기 = N > 이차원 배열 리스트를 통해 지도 만들기
# 1은 집이 있는 곳 > 탐색할 대상 > dfs 변수 설정
# 탐색 어떻게? > 델타
# 1이 연결되어 있는 곳을 찾아 
# 0은 없는 곳
# 연결이 끊기면 ans += 1

ans = 0

#델타 전역변수
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):#r,c는 좌표의 위치
    

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 조건: nr과 nc가 범위 안에 있고 nr과 nc가 1일 때 답에 추가
        if 0 <= nr < 16 and 0 <= nc < 16 and arr[nr][nc] == 1:


        #ans리스트에 1의 수 리턴하고 ans의 길이 구하면 답!



        if arr[nr][nc] == 1:
            visited

#탐색 시키기 위해 델타 호출
    if [r][c] == 1



#지도 만들기
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]




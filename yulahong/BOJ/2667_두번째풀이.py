# # 지도의 크기 = N > 이차원 배열 리스트를 통해 지도 만들기
# 1은 집이 있는 곳 > 탐색할 대상 > dfs 변수 설정
# 탐색 어떻게? > 델타
# 1이 연결되어 있는 곳을 찾아 
# 0은 없는 곳
# 연결이 끊기면 ans += 1
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):#r,c는 좌표의 위치
    visited[r][c] = True #방문 도장
    count = 1

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 조건: nr과 nc가 범위 안에 있고 nr과 nc가 1일 때 답에 추가
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] != True:
            count += dfs(nr, nc)
        
    return count

ans_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] != True:
            ans_list.append(dfs(i, j))

print(len(ans_list))
for a in sorted(ans_list):
    print(a)



        #ans리스트에 아파트 수 리턴하고 ans의 길이 구하면 답!






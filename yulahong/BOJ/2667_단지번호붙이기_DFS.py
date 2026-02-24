# 내가 해야할 일
# 변수 설정 - 1번
# 델타로 탐색 -3번
# visited 배열 설정 > 중복 탐색 제거 - 2번
# dfs함수 선언 > 그리드를 도는 함수 - 4번
# 첫번째 r,c 찾기

# 구해야하는 것
# 단지의 총 개수, 단지안에 있는 아파트 수 구하기

# 변수 설정
# 



N = int(input())
arr = [list(map(int, input())) for _ in range(N)] # 그리드 정보 받아오기
visited = [[0]*N for _ in range(N)] # 방문하면 1로 바꿔줄 0으로 채운 visited N*N 그리드


dr = [-1, 0, 1, 0] #델타 상 우 하 좌 만들기
dc = [0, 1, 0, -1]


#DFS함수 선언
def dfs(r, c):#r,c는 좌표의 위치
    visited[r][c] = True #방문 도장
    count = 1 #각 단지마다 아파트 수 저장할 count 변수 만들기, 방문하면 일단 1 할당

    for dir in range(4): #4방향 탐색
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 조건: nr과 nc가 범위 안에 있고/ 지도 그리드 nr과 nc가 1이고/ 방문하지 않지 않을 때
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] != True:
            count += dfs(nr, nc) #count 변수에 연결된 아파트를 더해줌
            # (0,0)(1,0)(1,1) L자 모양으로 붙어있는상황이면
            # DFS(0,0) 발견시 count = 1 실행 
            # dfs(1,0) 호출 > count = 1
            # dfs(1,1) 호출 > count = 1
            # 막다른 길 count += 1*3
        
    return count #함수가 끝날 때 카운트 리턴

ans_list = [] #아파트수를 저장해줄 새로운 리스트 만들기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] != True: # 2차원 배열을 돌면서 지도 그리드에서 1이고 방문하지 않은 좌표 (i, j)
            ans_list.append(dfs(i, j)) #dfs함수에 넣어주고 함수가 리턴한 값을 ans_list에 어펜드
            
print(len(ans_list)) #ans_list의 길이는 단지 수
for a in sorted(ans_list): #아파트 수 오름차순 정렬
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






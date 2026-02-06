#가장 큰 색칠 덩어리의 넓이 구하기

#2차원 격자 위에 직사각형들을 색칠했다. 
#색칠된 칸들 중에서 상하좌우로 이어진 하나의 덩어리를 한 그룹이라고 할 때, 
#가장 큰 그룹의 넓이를 구하라. 

# 터치패드에 정전기 에반데;;
# 패티 파이팅!!!
# 네 !!!!!!!!!!ㅜㅜㅜ 
from collections import deque #BFS너비우선탐색에서 큐로 쓸 deque불러오기

n = int(input()) #직사각형 개수 입력
MAX_R = 200 #보드 인덱스 최대값
OFFSET = 100 #음수좌표 대비 

rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
] # 사각형의 정보 입력 받기 * n줄

checked = [
    [0]*(MAX_R+1)
    for _ in range(MAX_R+1)
 ] #보드격자 1이면 칠해졌다는거 칠해졌는지 확인할 2차원 배열 

#직사각형들을 하나씩 꺼내서 보드에 칠하기 
for x1,y1,x2,y2 in rects: #순서 중요 
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = 1  # 그 칸을 칠했다. 



di = [1,-1,0,0]   #이웃칸을 찾는 버튼 
dj = [0,0,1,-1]


#방문배열 (BFS): visited[x][y]가 True면 (x,y)를 이미 BFS로 처리했다. 
visited = [[False]*(MAX_R+1)for _ in range(MAX_R+1)]

max_area = 0

for x in range(MAX_R+1): #새 덩어리 찾기 시작 
    for y in range(MAX_R+1):
        if checked[x][y] >= 1 and not visited[x][y]:  #칠해져있고 방문하지 않았을때  
            q = deque() #큐 생성 
            q.append((x,y)) #시작 칸 넣기 
            visited[x][y] = True #시작 칸 방문 처리 
            area =1 #현재 덩어리 넓이 

            while q: #큐가 빌 떄까지 
                cx, cy = q.popleft() #큐에서 하나 꺼내기 
                for k in range(4): #4방향 모두 검사하는데 
                    nx = cx +di[k] #이웃칸 x좌표 
                    ny = cy + dj[k] #이웃칸 y좌표 


                    if 0 <= nx <= MAX_R and 0 <= ny <= MAX_R: #보드 범위 안이면 
                    #칠해졌고 + 방문 안했으면 확장 
                        if checked[nx][ny] >= 1 and not visited[nx][ny]:
                            visited[nx][ny] = True #방문처리 
                            q.append((nx,ny)) #큐에 추가(확장)
                            area += 1 #덩어리 넓이 +1

            max_area = max(max_area,area) #BFS 끝났으면 이 덩어리 넓이로 최대값 갱신 

print(max_area) #최종 최대 덩어리 넓이 출력 
                
                




        


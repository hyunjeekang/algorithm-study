#####로직######
# 1. 배추좌표로 배추밭을 만든다.
# 2. 그 배추밭에서 시작배추를 찾는다. (이때 !!!!!!!!! 방문하지 않은걸로 해야겠죠?)
# 3. 시작배추를 기점으로 bfs를 통해 배추(1)만 담는다.
# 4. while q가 끝났다 == 배추가 없다 == 영역 한개 끝
# 5. cnt(영역) +1 

T = int(input())
q = []  # 빈 리스트 만듦 (여기에 배추위치 1만 도입예정)
dr = [-1,1,0,0]  #상하좌우
dc = [0,0,-1,1]

for tc in range(1,T+1):clear
    
    M,N,K = list(map(int,input().split()))  #M : 가로길이, N : 세로길이 , K : 배추의 위치 개수 
    arr = [[0]*M for _ in range(N)]  # 배추를 심기전에 밭을 만들자 ! 
    visited = [[False]*M for _ in range(N)]  # 방문배열 
    for k in range(K):  # 배추위치의 좌표값을 하나씩 받을거야 
        X,Y = list(map(int,input().split())) 
        arr[Y][X] = 1  # 여기까지 모든 좌표에 배추표시

    cnt = 0 #영역개수 초기화 
    for r in range(N):  # 행
        for c in range(M): # 열 
            if arr[r][c] == 1 and visited[r][c] == False:  ### 내가 놓친 부분 : 시작점이라도 방문하지 않은곳에서 시작해야지
                sr,sc = r,c #시작점 
                q.append((sr,sc)) 
                visited[sr][sc] = True #시작점 방문표시 
                #초기값 설정

                
                while q:
                    cr,cc = q.pop(0)  # 시작점 꺼내서 현재점으로 할당해주고 


                    for i in range(4):
                        #근데 주변에 한칸씩만 보고 그 주변에 1을 q에 넣기
                        nr = cr + dr[i] 
                        nc = cc + dc[i]

                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False: # 경계값 내에서 , 방문하지 않은것 
                            if arr[nr][nc] == 1: # 배추라면 
                                q.append((nr,nc)) #배추만 q에 넣기 
                                visited[nr][nc] = True
                cnt+=1  # while이 끝났다 == 주변에 배추 없음 == 영역 한개 끝 

    print(cnt)
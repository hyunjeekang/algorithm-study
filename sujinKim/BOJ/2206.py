# 벽 부수고 이동하기
# 이동 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면 한개까지 부수기 가능
import sys
input = sys.stdin.readline 
from collections import deque

dr = [-1,1,0,0] #상하좌우
dc = [0,0,-1,1]

N,M = map(int,input().split())  #1부터 시작 
arr = [list(map(int,input().strip())) for _ in range(N)] 
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
q = deque()
b = 0 # 0: 벽 아직 안부숨 , 1:벽 이미 부숨 


# for r in range(1,N+1):
#     for c in range(1,M+1):
r=c=0 # 시작점은 1,1 이니까 
cnt = 1 #이동거리
# if arr[r][c] == 0: ##
sr,sc = r,c  #초기값 설정
q.append((sr,sc,b,cnt)) 
visited[sr][sc][b] = True  #초기값 방문표시 

find = False
while q:
    cr,cc,cb,ccnt = q.popleft()

    if cr == N-1 and cc == M-1: ##
        find = True 
        print(ccnt)
        break
        
    for i in range(4):
        nr = cr +dr[i]
        nc = cc + dc[i]

        if 0<=nr<N and 0<=nc<M:
            if cb == 0: #벽을 안부순상태라면 
                if arr[nr][nc] == 0 and visited[nr][nc][0] == False : #갈곳이 있다면
                    q.append((nr,nc,cb+0,ccnt+1)) 
                    visited[nr][nc][0] = True
                elif arr[nr][nc]== 1 and visited[nr][nc][1] == False: # 갈곳이 없다면 
                    q.append((nr,nc,cb+1,ccnt+1)) #갈곳이 없다면 벽을 부순다.
                    visited[nr][nc][1] = True
            elif cb == 1: #벽을 부순 상태라면 
                if arr[nr][nc] == 0 and visited[nr][nc][1] == False: #오직 0인곳만 갈 수 있음
                    q.append((nr,nc,cb+0,ccnt+1))
                    visited[nr][nc][1]= True
                
if not find:
    print(-1)  ##
    



    





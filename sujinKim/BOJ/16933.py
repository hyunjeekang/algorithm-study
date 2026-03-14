# 벽 부수고 이동하기3
import sys
from collections import deque
input = sys.stdin.readline
# import os
# sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
# 0 : 이동 가능 / 1 : 이동할 수 없는 벽 
# (1,1) -> (N,M) 최단경로로 이동할라고
# 최단 경로 : 맵에서 가장 적은 개수의 칸을 지나는 경로를 말함 (시작하는칸,끝나는칸 포함)
# 이동하지 않고 같은 칸에 머물러있는 경우도 가능 -> 방문한 칸의 개수가 하나 늘어나느 것으로 생각 
# 낮과 밤이 번갈아가며 등장 (처음:낮,한 번 이동할때마다 바뀜)
# 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
# 벽을 K개까지 부수고 이동하여도 된다. (벽은 낮에만 부술 수 있음)
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인d접한 칸.
### 결론 : 최단 경로를 구해 내기

dr = [-1,1,0,0]  # 상하좌우
dc = [0,0,-1,1]
N,M,K = map(int,input().split())   # K : 부술 수 있는 벽의 개수  
# N개의 줄에 M개의 숫자로 맵이 주어진다. 
arr = [list(map(int,input().strip())) for _ in range(N)]  ###
# (1,1),(N,M)은 항상 0이라고 가정

## 제미나이 : 벽은 K개까지 부술 수 있어서 
visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]  # 방문배열+벽깸유무=3차원 
q = deque()

# 시작점 
cnt = 0 # 이동거리 
day = 0 # 낮,밤 유무 :낮=홀수, 밤=짝수 
b = 0  # 부신 횟수 
# for r in range(N):  # 1,1 ~ N,M이라 일부러 이렇게 표시,,하면 안되나봐 
#     for c in range(M):
        
#         if arr[r][c] == 0:
###제미나이
sr,sc = 0,0
q.append((sr,sc,cnt+1,day+1,b))
visited[0][sr][sc] = True # 시작점 방문쳌 

is_day = True 
find = False
while q:
    for _ in range(len(q)):
        cr,cc,ccnt,cday,cb = q.popleft() # 현재위치

        
        if cr == N-1 and cc == M-1:
            
            print(ccnt)
            find = True
            break 

        for i in range(4): # 현재위치에서 4방향을 볼건데 
            nr = cr + dr[i]  # 한칸씩 이동한 좌표 !! == 주변좌표들이 
            nc = cc + dc[i]

            if 0 <= nr < N and 0 <= nc < M: # 전체 경계췍
            

                # 이동할 곳이 0
                if arr[nr][nc] == 0 and not visited[cb][nr][nc]: # 아직 벽을 안꺴고, 방문도 안한상태 
                    # if arr[nr][nc] != 0 and cday %2 != 0: # 0이 아니고, cday가 홀수(낮)라면 
                    
                    visited[cb][nr][nc] = True # 깬 상태에서 방문처리
                    q.append((nr,nc,ccnt+1,cday+1,cb))
                # 이동할 곳이 벽(1)인 경우 
                elif arr[nr][nc] == 1 and cb < K and not visited[cb+1][nr][nc]:
                        if is_day:

                        # if cday % 2 != 0: #낮이먄? 부수고 이동
                            visited[cb+1][nr][nc] = True
                            q.append((nr,nc,ccnt+1,cday+1,cb+1)) ### 제미나이:밤에 벽을 만나면 그 자리에 머물기 
                        else:  # 밤이면? 머물다 꺠야함
                            q.append((cr,cc,ccnt+1,cday+1,cb))
        if find : break
    if find : break

    is_day = not is_day
if not find:
    print(-1)


                        
                # # 이미 다(?) 부심
                # if visited[1][nr][nc] == False and cb < K: #이미 부셨고, 방문은 안한상태
                #     if arr[nr][nc] == 0 : # 무조건 0일때만 이동할 수 있음 
                #         q.append((nr,nc,ccnt+1,cday+1))
                #         visited[1][nr][nc] = True # 이미 깼었으니까. 
                        

            # min = 9999999999
            # if ccnt <= min:
            #     min = ccnt

            # print(ccnt)

# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M, K = map(int, input().split())
# arr = [list(map(int, input().strip())) for _ in range(N)]

# # 방문 체크: visited[부순횟수][r][c]
# visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
# visited[0][0][0] = True

# q = deque([(0, 0, 0)]) # r, c, broken_count
# dist = 1
# is_day = True # 처음은 낮

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# while q:
#     # 현재 거리(dist)에서 갈 수 있는 모든 좌표를 한꺼번에 처리
#     for _ in range(len(q)):
#         cr, cc, cb = q.popleft()

#         if cr == N - 1 and cc == M - 1:
#             print(dist)
#             exit()

#         for i in range(4):
#             nr, nc = cr + dr[i], cc + dc[i]

#             if 0 <= nr < N and 0 <= nc < M:
#                 # 1. 빈 칸 이동
#                 if arr[nr][nc] == 0 and not visited[cb][nr][nc]:
#                     visited[cb][nr][nc] = True
#                     q.append((nr, nc, cb))
                
#                 # 2. 벽 부수기
#                 elif arr[nr][nc] == 1 and cb < K and not visited[cb + 1][nr][nc]:
#                     if is_day: # 낮이면 바로 부숨
#                         visited[cb + 1][nr][nc] = True
#                         q.append((nr, nc, cb + 1))
#                     else: # 밤이면? 이번 턴엔 못 가니까 '기다림' 예약 (좌표 그대로 다시 넣기)
#                         q.append((cr, cc, cb))

#     # 한 단계(낮 or 밤)가 끝나면 거리 1 증가, 낮밤 바뀜
#     dist += 1
#     is_day = not is_day

# print(-1)
                
                




            
            








# import sys
# sys.stdin = open("input.txt")
# from collections import deque
import heapq

# 차윤이 앞으로 이동,왼쪽으로 90도,오른쪽으로 90도 회전하는 RC카 선물받음
# 차윤이는 출발지에서 목적지까지 최소의 조작으로 이동시킬 수 있음.
# (최단거리가 아닌, 최소 리모컨 조작 횟수임을 유의)
# 차윤이는 항상 위를 바라보는 상태로 RC카의 조작을 시작한다.
### 4차원이어야하는 이유 : 변수가 행,열,나무벤횟수,rc카의 방향까지
dr = [0,0,-1,1] # 0:좌 , 1:우, 2:상, 3:하
dc = [-1,1,0,0]
T = int(input())
INF = float('inf')
for tc in range(1,T+1):
    N,K = map(int,input().split()) # 필드의 크기/나무 벨 수 있는 횟수
    arr = [input() for _ in range(N)]
    visited = [[[[INF]*4 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    # visited = [[[0]*(K+1) for _ in range(N)] for _ in range(N)]
    # print(arr)

    for r in range(N):
        for c in range(N):
            if arr[r][c] == "X": # 시작점을 찾았더라면
                sr,sc = r,c # 시작점 정하기
                sk = 0 # 나무를 벤 횟수
                # (행,열,벤 횟수, 현재 방향)
                # q.append((sr,sc,sk,2))
                # visited[sr][sc][0][2] = 1 # 시작점 방문 표시

    pq = []
    heapq.heappush(pq, (0, sr, sc, 0, 2))
    visited[sr][sc][0][2] = 0




    ans = -1 # 길을 못 찾을 경우 (일단 못찾았다고 가정)
    while pq:
        # cr,cc,ck,cd = q.popleft() # 현재값 설정 # cd : 현재 보고 있는 방향
        #
        # # 종료조건
        # if arr[cr][cc] == "Y": #RC카를 이동 시키고자 하는 위치로 왔다면
        #     ans = visited[cr][cc][ck][cd] -1 # 방문배열에 시작할때 1로 표시했던거 다시 빼주는거
        #
        #     break
        dist, cr, cc, ck, cd = heapq.heappop(pq)


        if visited[cr][cc][ck][cd] < dist:
            continue


        if arr[cr][cc] == "Y":
            ans = dist
            break



        for i in range(4): # i : 내가 가려는 방향
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N: # 주변값 경계췍
                # 방향
                if i == cd:
                    cost = 1
                elif (cd == 2 and i == 3) or (cd == 3 and i == 2) or (cd == 0 and i == 1) or (cd == 1 and i == 0):
                    cost = 3
                else:
                    cost = 2

                new_dist = dist + cost
                # if (arr[nr][nc] == "G" or arr[nr][nc] == "Y") and not visited[nr][nc][ck][i]:
                #     visited[nr][nc][ck][i] = visited[cr][cc][ck][cd] + cost
                #     q.append((nr,nc,ck,i))
                    # 1. 길(G) 또는 목적지(Y)일 때
                if (arr[nr][nc] == "G" or arr[nr][nc] == "Y"):
                    if visited[nr][nc][ck][i] > new_dist:  # 더 짧은 경로 발견!
                        visited[nr][nc][ck][i] = new_dist
                        heapq.heappush(pq, (new_dist, nr, nc, ck, i))

                # # 나무 만나면 : (ck + 1) 다음 층으로 이동
                # elif arr[nr][nc] == "T" and ck < K: # 아직 더 벨 수 있다면
                #     if not visited[nr][nc][ck+1][i]:
                #         # 현재 위치까지 오는데 걸린 칸 수에 1을 더해서, 나무를 하나 더 벤 상태의 방문 기록에 저장한다.
                #         visited[nr][nc][ck+1][i] = visited[cr][cc][ck][cd] + cost
                #         q.append((nr,nc,ck+1,i))
                # 필요없을듯 : 위에서 이미 필터링 하고 있어서
                # elif arr[nr][nc] == "T" and ck > K:
                # 2. 나무(T)를 만났을 때
                elif arr[nr][nc] == "T" and ck < K:
                    if visited[nr][nc][ck + 1][i] > new_dist:
                        visited[nr][nc][ck + 1][i] = new_dist
                        heapq.heappush(pq, (new_dist, nr, nc, ck + 1, i))

    print(f'#{tc} {ans}')







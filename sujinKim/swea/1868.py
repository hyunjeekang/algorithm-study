
from collections import deque


dr = [0,0,-1,1,-1,1,-1,1] # 좌,우,상,하,좌상,좌하,우상,우하
dc = [-1,1,0,0,-1,-1,1,1]

T = int(input())
for tc in range(1,T+1):

    N = int(input()) # 지뢰찾기를 하는 표의 크기가 N*N
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    result = [[0]*N for _ in range(N)] # 지뢰의 개수를 담을 표시칸
    visited = [[False]*N for _ in range(N)] # 갔던곳인지 정도는 표시해야함 

    # 1. "."에 주변 지뢰 갯수를 세자
    for r in range(N):
        for c in range(N):
            if arr[r][c] == ".": # 우선 "."과 "*"로 입력받은 배열을 탐색하면서
    # "."이라면, 그 주변을 봐서 "*"의 개수를 입력 받는다.
                for i in range(8): # 8방향 볼건데
                    nr = r + dr[i]
                    nc = c + dc[i]

                    # 경계췍
                    if 0 <= nr < N and 0 <= nc < N:
                        # 주변에 "*"가 있다면
                        if arr[nr][nc] == '*':
                            result[r][c] += 1 # 주변에 "*"이 있으면 그곳에 +1씩 계속 하기 
    # for k in range(N):
    #     for p in range(N):
    #         if result[k][p] == 0:
    #             # 그 주변까지 싹 터짐

    # 연쇄 폭발을 일으킬 BFS 함수
    def bfs(sr,sc):
        q = deque([(sr,sc)]) # 시작점으로 시작(?) => 이부분 잘 안와닿음 
        visited[sr][sc] = True

        while q:
            r,c = q.popleft() # q에 있는걸 꺼내가지고

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                # 맵 범위 안이면서, 아직 안열린 빈칸이라면 ?
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] == ".":
                    visited[nr][nc] = True

                    if result[nr][nc] == 0: # 0이라면
                        q.append((nr,nc)) # 주변값 담아야지

    ans = 0

    # 2. 0을 찾아서, 그 주변 9방향 싹 없애기
    for k in range(N):
        for p in range(N):
            if arr[k][p] == '.' and result[k][p] == 0 and not visited[k][p]:
                ans += 1 # 0인 칸을 클릭했으니까 +1
                bfs(k,p) # 클릭한 지점에서 연쇄 폭발하는 함수 실행

    # 3. 폭발하고 남은 "." 개수 세기
    for d in range(N):
        for e in range(N):
            if arr[d][e] == '.' and not visited[d][e]:
                ans += 1
    print(f'#{tc} {ans}')
































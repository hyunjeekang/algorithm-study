from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):#r,c는 좌표의 지점
    q = deque([(r, c)]) #r,c가 쌍으로 들어감

    arr[r][c] = 0
    count = 1   

    while q: #q가 0이 될 때까지
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            # 조건: nr과 nc가 범위 안에 있고 nr과 nc가 1일 때 답에 추가
            
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] != True:
                visited[nr][nc] = 1
                q.append((nr, nc))
                count += 1

    return count

ans_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] != True:
            ans_list.append(bfs(i, j))
            
print(len(ans_list))
for a in sorted(ans_list):
    print(a)




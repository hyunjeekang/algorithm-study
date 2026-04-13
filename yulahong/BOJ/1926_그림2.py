from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split()) for _ in range(n))]
visited = [ [0]*m for _ in range(n) ]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0
# maxp = 0

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    maxp = 0

    while q:
        cr, cc = q.popleft()
        maxp += 1

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    visited[nr][nc] = 1

        return maxp


# 시작점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            maxp = max(maxp, bfs(i, j)) 

print(cnt)
print(maxp)



    
# bfs함수 호출
    # 델타  
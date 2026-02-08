from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]
# Please write your code here.
is_found = False
que = deque([(0, 0)])
visited[0][0] = True
while que :
    x, y = que.popleft()
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m :
            if a[x+dx[i]][y+dy[i]] == 1 and not visited[x+dx[i]][y+dy[i]]:
                visited[x+dx[i]][y+dy[i]] = True
                que.append((x+dx[i], y+dy[i]))
        if x+dx[i] == n-1 and y+dy[i] == m-1 :
            print(1)
            is_found = True
            break
    if is_found :
        break
else :
    print(0)
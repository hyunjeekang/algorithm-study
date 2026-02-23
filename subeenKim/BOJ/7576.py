from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
q = deque([])
green_tomato = False
for x in range(N):
    for y in range(M):
        if tomato[x][y] == -1 :
            visited[x][y] = True
        elif tomato[x][y] == 1:
            q.append((x, y, 0))
            visited[x][y] = True
        else :
            green_tomato = True

if green_tomato:
    while q :
        X, Y, cnt = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = X+dx, Y+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = True

    not_yet_red = False
    for x in visited:
        if False in x:
            not_yet_red = True
            break
    
    if not_yet_red :
        print(-1)
    else :
        print(cnt)

else : # 이미 모든 토마토가 익어 있는 상태
    print(0)
from collections import deque
import sys; input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]

def break_walls():
    visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
    q = deque([(0, 0, 0, 1)])
    visited[0][0][0] = 1

    while q :
        broken, x, y, dist = q.popleft()
        if x == N-1 and y == M-1:
            return dist
        
        should_stay = False
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and visited[broken][nx][ny] == 0:
                if broken == K: # 더 이상 벽을 부술 수 없음
                    if grid[nx][ny] == '0':
                        q.append((broken, nx, ny, dist+1))
                        visited[broken][nx][ny] = dist + 1

                else: # 벽을 더 부술 수 있는 횟수가 남아있을 때
                    if dist % 2 == 0: # 밤이면 벽 못 부숨
                        if grid[nx][ny] == '1':
                            should_stay = True
                        else:
                            q.append((broken, nx, ny, dist+1))
                            visited[broken][nx][ny] = dist + 1
                    else: # 낮이면 벽 부수기 가능
                        if grid[nx][ny] == '0':
                            q.append((broken, nx, ny, dist+1))
                            visited[broken][nx][ny] = dist + 1
                        else: # 벽 부수기!
                            q.append((broken+1, nx, ny, dist+1))
                            visited[broken+1][nx][ny] = dist + 1
        if should_stay:
            q.append((broken, x, y, dist+1))

    return -1

print(break_walls())
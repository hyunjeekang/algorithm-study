from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    grid = [[0]*51 for _ in range(51)]
    dist = [[-1]*51 for _ in range(51)]
    for ax, ay, bx, by in rectangle:
        for x in range(ax, bx):
            for y in range(ay, by):
                grid[x][y] = 1
                
    dist[characterX][characterY] = 0
    q = deque([(characterX, characterY)])
    while q:
        x, y = q.popleft()
        if x == itemX and y == itemY:
            break
        for dx, dy, drc in [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < 51 and 0 <= ny < 51) and (dist[nx][ny] == -1):
                if drc == 0:
                    if (y-1 < 0 and grid[x-1][y] == 1) or (grid[x-1][y-1] + grid[x-1][y] == 1):
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
                elif drc == 1:
                    if (x-1 < 0 and grid[x][y] == 1) or (grid[x-1][y] + grid[x][y] == 1):
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
                elif drc == 2:
                    if (y-1 < 0 and grid[x][y] == 1) or (grid[x][y-1] + grid[x][y] == 1):
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
                else:
                    if (x-1 < 0 and grid[x][y-1] == 1) or (grid[x-1][y-1] + grid[x][y-1] == 1) :
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
    answer = dist[itemX][itemY]    
    return answer
from collections import deque

tc = int(input())

def how_many_times():
    L = int(input())
    nx, ny = map(int, input().split())
    gx, gy = map(int, input().split())
    if nx == gx and ny == gy :
        return 0
    
    grid = [[0]*L for _ in range(L)]

    q = deque([(nx, ny)])
    while q :
        x, y = q.popleft()
        for dx, dy in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
            i, j = x+dx, y+dy
            if i == gx and j == gy :
                return grid[x][y] + 1
            if 0 <= i < L and 0 <= j < L and grid[i][j] == 0:
                grid[i][j] = grid[x][y] + 1
                q.append((i, j))

for _ in range(tc):
    print(how_many_times())
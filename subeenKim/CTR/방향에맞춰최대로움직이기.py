N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
directions = [list(map(int, input().split())) for _ in range(N)]
dir_dict = {1:(-1, 0), 2:(-1, 1), 3:(0, 1), 4:(1, 1), 5:(1, 0), 6:(1, -1), 7:(0, -1), 8:(-1, -1)}
r, c = map(int, input().split())
# Please write your code here.
def backtrack(x, y, cnt):
    global max_count
    v = grid[x][y]
    dx, dy = dir_dict[directions[x][y]]
    nx, ny = x, y
    while True:
        nx, ny = nx+dx, ny+dy
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny] > v and not visited[nx][ny]:
                visited[nx][ny] = True
                backtrack(nx, ny, cnt+1)
                visited[nx][ny] = False
        else:
            max_count = cnt if cnt > max_count else max_count
            return

visited = [[False]*N for _ in range(N)]
visited[r-1][c-1] = True
max_count = 0
backtrack(r-1, c-1, 0)
print(max_count)
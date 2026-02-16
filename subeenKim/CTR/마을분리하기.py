n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def dfs(grid, x, y, visited):
    global people
    visited[x][y] = True

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                people += 1
                dfs(grid, nx, ny, visited)
    return people

village = 0
visited = [[False]*n for _ in range(n)]
people_cnt = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1 and not visited[x][y]:
            village += 1
            people = 1
            people_cnt.append(dfs(grid, x, y, visited))
people_cnt.sort()

print(village)
for pc in people_cnt:
    print(pc)
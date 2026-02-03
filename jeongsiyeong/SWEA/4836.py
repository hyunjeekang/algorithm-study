# SWEA 4836 색칠하기

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    grid = [[(0,0)] * 10 for _ in range(10)]
    for i in range(n):
        a_x, a_y, b_x, b_y, color = map(int, input().split())
        for x in range(a_x, b_x):
            for y in range(a_y, b_y):
                if color == 1:
                    grid[x][y] = (grid[x][y][0] + 1, grid[x][y][1])
                else:
                    grid[x][y] = (grid[x][y][0], grid[x][y][1] + 1)
    result = 0
    for x in range(10):
        for y in range(10):
            if grid[x][y][0] > 0 and grid[x][y][1] > 0:
                result += 1
    print(f"#{test_case} {result}")
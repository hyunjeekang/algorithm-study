N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[[] for _ in range(N)] for _ in range(N)] # 각 칸마다 그 칸까지 이동할 때의 (max, min) 값 저장

dp[0][0].append((grid[0][0], grid[0][0]))
for y in range(1, N):
    ma, mi = dp[0][y-1][0]
    dp[0][y].append((max(ma, grid[0][y]), min(mi, grid[0][y])))
for x in range(1, N):
    ma, mi = dp[x-1][0][0]
    dp[x][0].append((max(ma, grid[x][0]), min(mi, grid[x][0])))

for x in range(1, N):
    for y in range(1, N):
        for maxnum, minnum in dp[x-1][y]:
            up_max, up_min = max(maxnum, grid[x][y]), min(minnum, grid[x][y])
            dp[x][y].append((up_max, up_min))
        for maxnum, minnum in dp[x][y-1]:
            left_max, left_min = max(maxnum, grid[x][y]), min(minnum, grid[x][y])
            dp[x][y].append((left_max, left_min))

        temp_list = []
        for maxnum, minnum in dp[x][y]:
            no_need = False
            for ma, mi in dp[x][y]:
                if maxnum > ma and minnum < mi:
                    no_need = True
                    break
            if not no_need:
                temp_list.append((maxnum, minnum))
        dp[x][y] = set(temp_list).copy()


diff = float('inf')
for ma, mi in dp[N-1][N-1]:
    if diff > ma - mi :
        diff = ma - mi
print(diff)
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

def is_range(r,c):
    return 0<=r<N and 0<=c<N

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for r in range(N):
    for c in range(N):
        if arr[r][c]:
            continue
        if c > 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
        if r > 0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
        if r > 0 and c > 0:
            if not arr[r-1][c] and not arr[r][c-1]:
                dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] +dp[r-1][c-1][2]

print(sum(dp[N-1][N-1]))
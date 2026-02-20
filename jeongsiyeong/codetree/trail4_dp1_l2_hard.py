#정수 사각형 차이의 최소 2
INF = float('inf')
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = INF

for cutline in range(1, 101):
    dp = [[INF]*N for _ in range(N)]

    if cutline > arr[0][0]:
        continue

    dp[0][0] = arr[0][0]

    for c in range(1, N):
        if arr[0][c] >= cutline: 
            dp[0][c] = max(dp[0][c-1], arr[0][c])
    for r in range(1, N):
        if arr[r][0] >= cutline:
            dp[r][0] = max(dp[r-1][0], arr[r][0])
    for r in range(1, N):
        for c in range(1, N):
            if arr[r][c] >= cutline:
                dp[r][c] = max(arr[r][c], min(dp[r-1][c], dp[r][c-1]))
    if dp[N-1][N-1] != INF:
        ans = min(ans, dp[N-1][N-1] - cutline)
print(ans)
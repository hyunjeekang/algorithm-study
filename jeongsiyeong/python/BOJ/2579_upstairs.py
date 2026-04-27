N = int(input())

stairs = [0] * N
for i in range(N):
    stairs[i] = int(input())

dp = [0] * N

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(N):
    if i+2 < N:
        dp[i+2] = max(dp[i] + stairs[i+2], dp[i+2])
    if i+3 < N :
        dp[i+3] = max(dp[i] + stairs[i+2] + stairs[i+3], dp[i+3])

print(dp[N-1])

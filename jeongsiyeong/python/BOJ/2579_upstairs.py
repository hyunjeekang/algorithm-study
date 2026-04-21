N = int(input())

stairs = []

for _ in range(N):
    a = int(input())
    stairs.append(a)

dp = [0] * (N+1)

for i in range(N):
    if i+2 <=N-1:
    #+2
        dp[i+2] = max(dp[i]+stairs[i], dp[i+2])
    if i+3 <=N-1:
    #+1+2
        dp[i+3] = max(dp[i]+stairs[i]+stairs[i+1], dp[i+3])

print(dp[N-1]+stairs[N-1])

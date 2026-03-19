import sys
input = sys.stdin.readline

N = int(input())
INF = float('inf')
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (1<<N) for _ in range(N)]


def dfs(start, visited):
    if visited == (1<<N) - 1:
        if arr[start][0] != 0:
            return arr[start][0]
        else:
            return INF
        
    if dp[start][visited] != -1:
        return dp[start][visited]
    
    dp[start][visited] = INF
    
    for i in range(1, N):
        if not (visited & (1 << i)) and arr[start][i] != 0:
            dp[start][visited] = min(dp[start][visited], dfs(i, visited|(1<<i)) + arr[start][i])
    
    return dp[start][visited]

print(dfs(0, 1))
import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [-1]*N

def solve(n):
    # 기본값
    if n==0:
        dp[0] = 1
        return 1

    # 메모이제이션 (이미 값을 구해놨던 것)
    if dp[n] != -1:
        return dp[n]
    
    # 새로 구해야 하는 값
    max_prev = 0
    for i in range(n):
        if A[i] < A[n]:
            max_prev = max(max_prev, solve(i))
    dp[n] = max_prev + 1
    return dp[n]

# 앞에 계산 안 된 값이 있을수도 있으니까 다시 다 채우기?
for i in range(N):
    solve(i)
result = max(dp)

print(result)
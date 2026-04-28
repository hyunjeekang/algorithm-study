N = int(input())
scores = list(int(input()) for _ in range(N))

dp = [0]*N

for i in range(N):
    if i==0:
        dp[0] = scores[0]
    elif i==1:
        dp[1] = scores[0]+scores[1]
    elif i==2:
        dp[2] = max(scores[0]+scores[2], scores[1]+scores[2])
    else:
        dp[i] = max(dp[i-3]+scores[i-1]+scores[i], dp[i-2]+scores[i])

print(dp[N-1])

# def solve(n):
#     if n == 0: return scores[0]
#     if n == 1: return scores[0]+scores[1]
#     if n == 2: return max(scores[0]+scores[2], scores[1]+scores[2])
    
#     if dp[n] != 0:
#         return dp[n]
    
#     dp[n] = max(solve(n-3) + scores[n-1], solve(n-2)) + scores[n]
#     return dp[n]

# print(solve(N-1))

#동전 프로모션
#A타입의 동전:특별동전->같은 종류의 동전을 여러 번 사용하여 거슬러 줄 수 있음
#B타입의 동전:한정동전->각 종류별로 한번만 사용가능

#최소한의 동전만을 사용하여 거슬러서

#동전 종류의 수 n, 거슬러줘야 하는 금액 m
n, m = map(int, input().split())

dp = [float('inf')] * (m + 1)
dp[0] = 0

coins = []
for _ in range(n):
    t, c = input().split()
    coins.append((t,int(c)))

for t,c in coins:
    if t == 'A':
        for j in range(c, m+1):
            if dp[j-c] != float('inf'):
                dp[j] = min(dp[j], dp[j-c] + 1)
    else:
        for j in range(m, c-1, -1):
            if dp[j-c] != float('inf'):
                dp[j] = min(dp[j], dp[j-c] + 1)

print(dp[m] if dp[m] != float('inf') else -1)
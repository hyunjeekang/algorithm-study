T = int(input())
 
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    use = list(map(int, input().split()))
 
    dp = [0]*13
 
     
    for i in range(1, 13):
        # 1일권 & 1달권
        day_price = cost[0]*use[i-1]
        month_price = cost[1]
        dp[i] = dp[i-1] + min(day_price, month_price)
 
        # 3달권
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + cost[2])
        else:
            dp[i] = min(dp[i], cost[2])
     
    # 1년권과 비교하기
    ans = min(dp[12], cost[3])
    print(f'#{tc} {ans}')
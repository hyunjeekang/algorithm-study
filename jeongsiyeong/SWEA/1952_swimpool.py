T = int(input())

for test_case in range(1, T+1):
    costs = list(map(int, input().split()))
    #1일, 1달, 3달, 1년
    
    months = list(map(int, input().split()))
    
    dp = [0] * 13
    
    dp[0] = 0
    
    for i in range(1, 13):
        month_cost = min(months[i-1]*costs[0], costs[1])
        
        dp[i] = dp[i-1] + month_cost
        
        if i>=3:
            dp[i] = min(dp[i], dp[i-3] + costs[2])
    answer = min(dp[12], costs[3])
    
    print(f'#{test_case} {answer}')        
            
T = int(input())

INF = float('inf')

for test_case in range(1, T+1):
    string = list(map(int, input().split()))
    
    N = string[0]
    
    charges = string[1:]
    dp = [INF] * N
    dp[0] = 0
    
    for i in range(N-1):
        if dp[i] == INF:
            continue
        for step in range(1, charges[i]+1):
            next_pos = i + step
            
            if next_pos < N:
                dp[next_pos] = min(dp[next_pos], dp[i] + 1)
    
    print(f'#{test_case} {dp[N-1] - 1}')     
    
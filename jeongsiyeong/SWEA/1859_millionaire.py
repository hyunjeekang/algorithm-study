T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    mx_dp = [0] * N
    mx_dp[N-1] = arr[N-1]
    for i in range(N-2, 0, -1):
        mx_dp[i] = max(mx_dp[i+1], arr[i])
    answer = 0
    for i in range(N-1):
        if arr[i] < mx_dp[i+1]:
            answer += mx_dp[i+1] - arr[i]
    
    print(f'#{test_case} {answer}')
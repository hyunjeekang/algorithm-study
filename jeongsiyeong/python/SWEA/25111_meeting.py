MOD = int(1e9 + 9)
T = int(input())

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())

    w = n - m
    
    safe_capacity = (w + 1) * (k - 1)
    
    if m <= safe_capacity:
        answer = m
    else:
        c = m - w * (k - 1)
        
        b = c // k
        
        first_block_score = (2 * k * (pow(2, b, MOD) - 1)) % MOD
        
        rem_score = m - (b * k)
        
        answer = first_block_score + rem_score
        
    print(f'{answer % MOD}')
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_fly = 0
    
    for s_r in range(N - M + 1):
        for s_c in range(N - M + 1):
            
            total = 0
            
            for r in range(s_r, s_r + M):
                for c in range(s_c, s_c + M):
                    total += arr[r][c]  
                    
            max_fly = max(max_fly, total)
            
    print(f"#{test_case} {max_fly}")
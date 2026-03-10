T = int(input())

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = -1
    
    for r in range(N - 2):
        for c in range(1, N - 1):
            
            for a in range(1, N):
                for b in range(1, N):
                    
                    if (a + b) * 2 <= result:
                        continue
                    
                    if c + a >= N or c - b < 0 or r + a + b >= N:
                        continue
                    
                    visited = [False] * 101
                    is_able = True
                    cur_r, cur_c = r, c
                    
                    lengths = [a, b, a, b]
                    
                    for i in range(4):
                        for _ in range(lengths[i]):
                            cur_r += dr[i]
                            cur_c += dc[i]
                            
                            dessert = arr[cur_r][cur_c]
                            
                            if visited[dessert]:
                                is_able = False
                                break
                            
                            visited[dessert] = True
                        
                        if not is_able:
                            break
                    
                    if is_able:
                        result = max(result, (a + b) * 2)
                        
    print(f'#{test_case} {result}')
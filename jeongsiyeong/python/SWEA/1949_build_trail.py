import sys
sys.stdin = open("algorithm-study\jeongsiyeong\SWEA\sample_input (2).txt")

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(r, c, chance, length):
    global mx_length
    mx_length = max(length, mx_length)
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if is_range(nr, nc) and not visited[nr][nc]:
            if arr[nr][nc] < arr[r][c]:
                visited[nr][nc] = True
                dfs(nr, nc, chance, length + 1)
                visited[nr][nc] = False
            
            elif chance == 1 and arr[nr][nc] - K < arr[r][c]:
                visited[nr][nc] = True
                original_height = arr[nr][nc]
                
                arr[nr][nc] = arr[r][c] - 1
                
                dfs(nr, nc, 0, length + 1)
                
                arr[nr][nc] = original_height
                visited[nr][nc] = False
            
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    mx_high = max(map(max, arr)) 
    
    highs = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == mx_high:
                highs.append((r, c))
                
    mx_length = 0
    for h_r, h_c in highs:
        visited = [[False] * N for _ in range(N)]
        
        visited[h_r][h_c] = True
        dfs(h_r, h_c, 1, 1)
    
    print(f'#{test_case} {mx_length}')
T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r,c):
    return 0<=r<4 and 0<=c<4

def dfs(cur_r, cur_c, result, depth):
    if depth == 6:
        results.add(result)
        return
    
    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if is_range(nr,nc) :
            dfs(nr, nc, result+arr[nr][nc], depth+1)
            

for test_case in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    
    results = set()
    
    
    for r in range(4):
        for c in range(4):
            dfs(r, c, arr[r][c], 0)
    
    print(f'#{test_case} {len(results)}')
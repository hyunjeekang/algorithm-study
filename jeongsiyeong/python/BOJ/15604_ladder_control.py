N, M, H = map(int, input().split())

ladders = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    
    ladders[a][b] = 1
    
def check():
    for c in range(1, N+1):
        start_c = c
        for i in range(1, H+1):
            if ladders[i][start_c]:
                start_c+=1
            elif ladders[i][start_c-1]:
                start_c-=1
        if start_c != c:
            return False
    return True

ans = 4

def dfs(r, depth):
    global ans
    
    if depth > 3 or depth>=ans:
        return
    
    if check():
        ans = min(ans, depth)
        return
    
    for i in range(r, H+1):
        for j in range(1, N):
            if not ladders[i][j]:
                if not ladders[i][j-1] and not ladders[i][j+1]:
                    ladders[i][j] = 1
                    dfs(i, depth + 1)
                    ladders[i][j] = 0
dfs(1,0)

if ans<=3:
    print(ans)
else:
    print(-1)
            
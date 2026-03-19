T = int(input())

def dfs(depth, cur_prob):
    global answer
    
    if cur_prob <= answer:
        return
    
    if depth == N:
        answer = max(answer, cur_prob)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, cur_prob*(arr[depth][i] / 100))
            visited[i] = False
    
for test_case in range(1, T+1):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    visited = [False] * N
    dfs(0, 1.0)
    
    print(f'#{test_case} {answer*100:.6f}')
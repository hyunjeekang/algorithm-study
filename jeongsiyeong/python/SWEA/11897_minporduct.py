T = int(input())

def dfs(depth):
    global answer
    global result
    if answer < result:
        return
    
    if depth == N:
        answer = min(answer, result)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result += arr[depth][i]
            dfs(depth+1)
            result -= arr[depth][i]
            visited[i] = False

for test_case in range(1, T+1):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')
    
    for i in range(N):
        visited = [False] * N
        result = 0
        visited[i] = True
        result += arr[0][i]
        dfs(1)
    
    print(f'#{test_case} {answer}')
    
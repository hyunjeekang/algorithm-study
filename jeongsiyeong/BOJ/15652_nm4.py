def dfs(start,depth):
    if depth == M:
        print(*result)
        return
    for i in range(start, N+1):
        result[depth] = i
        dfs(i, depth+1)
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    result = [0] * M
    dfs(1,0)
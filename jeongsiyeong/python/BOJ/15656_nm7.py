def dfs(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        result[depth] = arr[i]
        dfs(depth+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = [0]*M
    dfs(0)
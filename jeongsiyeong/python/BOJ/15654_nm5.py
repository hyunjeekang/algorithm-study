def dfs(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            result[depth] = arr[i]
            visited[i] = True
            dfs(depth+1)
            visited[i] = False

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = [0]* M
    visited = [False] * N
    dfs(0)


def dfs(start, depth):
    if depth == M:
        ans.add((tuple(result)))
        return
    for i in range(start, N):
        result[depth] = arr[i]
        dfs(i+1, depth+1)

if __name__=="__main__":
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = [0]*M
    ans = set()
    dfs(0,0) 
    for a in ans:
        print(*a)
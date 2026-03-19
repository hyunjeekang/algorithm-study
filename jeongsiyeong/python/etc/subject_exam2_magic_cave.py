T = int(input())

def dfs(node, curr_dp):
    next_dp = curr_dp[:]
    w = weight[node]
    v = value[node]
    
    for i in range(K, w-1, -1):
        if next_dp[i] < next_dp[i-w] + v:
            next_dp[i] = next_dp[i-w] + v
    
    if not tree[node]:
        current_max = 0
        
        for i in range(K+1):
            if next_dp[i] > current_max:
                current_max = next_dp[i]
        if current_max > ans[0]:
            ans[0] = current_max
    else:
        for child in tree[node]:
            dfs(child, next_dp)

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    
    tree = [[] for _ in range(N+1)]
    weight = {}
    value = {}
    root = 0
    
    for _ in range(N):
        r, w, v, p = map(int, input().split())
        weight[r] = w
        value[r] = v
        
        if p==0:
            root = r
        else:
            tree[p].append(r)
    ans = [0]
    
    initial_dp = [0] * (K+1)
    dfs(root, initial_dp)
    
    print(f'#{test_case} {ans[0]}')
    

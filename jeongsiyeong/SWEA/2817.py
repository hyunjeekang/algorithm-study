T = int(input())

def dfs(index, cur_sum):
    global cnt
    
    if cur_sum > K:
        return
        
    if index == N:
        if cur_sum == K:
            cnt += 1
        return
    
    dfs(index + 1, cur_sum + arr[index])
    
    dfs(index + 1, cur_sum)

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    cnt = 0    
    dfs(0, 0)
    
    print(f'#{test_case} {cnt}')
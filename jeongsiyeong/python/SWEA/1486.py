T = int(input())

def dfs(index, current_height):
    global answer
    
    if current_height - B >= answer:
        return
    
    if current_height >= B:
        answer = min(answer, current_height - B)
        return
    
    if index == N:
        return
        
    dfs(index + 1, current_height + arr[index])
    
    dfs(index + 1, current_height)

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    
    answer = float('inf')

    dfs(0, 0)
    
    print(f'#{test_case} {answer}')
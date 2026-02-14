def backtrack(k, N, current_sum):
    global min_val
    # 중간까지의 합이 이미 min_val을 넘어서는 경우 종료!!
    if current_sum >= min_val:
        return
    # 모든 행 다 선택 완료
    if k == N :
        min_val = current_sum # 위에서 합이 min_val 이상인 경우는 미리 끝냈으므로 이 조건문이 수행되면 합이 min_val보다 더 작다는 뜻
    else :
        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                backtrack(k+1, N, current_sum + grid[k][i])
                visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    min_val = float('inf')
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    order = [0]*N
    visit = [0]*N
    perm = []
    backtrack(0, N, 0)
    print(f'#{tc} {min_val}')
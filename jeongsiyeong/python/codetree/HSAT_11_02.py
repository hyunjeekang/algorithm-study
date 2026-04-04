#편안한 워크숍
#N*N 격자 각 칸 수는 높이
#가장 편안한 등산로 찾기(최적해)-인접한 높이의 차들간의 최댓값이 최소
#시작은 상관 없음
#이동할때마다 높이가 높아져야합니다(오르막길?)
#등산로 길이 최소 K
#첫 번째 줄에 가장 편안한 등산로의 인접한 높이의 차들 간의 최댓값 출력
#만약 조건을 만족하는 등산로를 만들 수 없는 경우 -1을 출력
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def is_range(r, c):
    return 0<=r<N and 0<=c<N

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

max_diff = 0
for r in range(N):
    for c in range(N):
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            
            if is_range(nr, nc) and arr[nr][nc] > arr[r][c]:
                max_diff = max(max_diff, arr[nr][nc] - arr[r][c])
                
def check(limit):
    dp = [[-1] * N for _ in range(N)]
    
    def dfs(r, c):
        if dp[r][c] != -1:
            return dp[r][c]
        
        dp[r][c] = 1
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_range(nr, nc):
                diff = arr[nr][nc] - arr[r][c]
                if 0<diff<=limit:
                    dp[r][c] = max(dp[r][c], 1+dfs(nr,nc))
        return dp[r][c]

    for r in range(N):
        for c in range(N):
            if dfs(r, c) >= K :
                return True
    return False

left, right = 0, max_diff
answer = -1

while left <= right:
    mid = (left + right) // 2
    
    if check(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
            
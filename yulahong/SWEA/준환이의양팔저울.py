#시간 초과나지만 결과는 나오는 풀이
# N 개의 무게추
# 모든 무게추를 양팔저울 위에 올리는 순서는 N!> 좌우 정하기 2^N * N!
# 항상 좌 >= 우
def scale (cnt, left_sum, right_sum):

    global ans

    if right_sum > left_sum:
        return
    if cnt == N :
        ans += 1
        return

    for idx in range(N):
        if visited[idx]:
            continue

        visited[idx] = 1
        scale(cnt+1, left_sum + weight[idx], right_sum)
        scale(cnt+1, left_sum, right_sum + weight[idx])
        visited[idx] = 0 #순열은 무조건 방문처리 빼주기


#변수
T = int(input())
# 로직
# 순열
# dfs
# 백트래킹 > 왼쪽이 오른쪽보다 무거우면 ㄱㅊ은 경우의 수 출력

for tc in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))
    visited = [0]*N
    ans = 0

    scale(0, 0, 0)

    print(f'#{tc} {ans}')


#강사님이 알려주신 풀이

def dfs(count, visited, left, right):
      
    if count == N:
        return 1
      
    if dp[visited].get(left):
        return dp[visited][left]
      
    temp = 0
    for i in range(N):
        if visited & (1 << i):
            continue
          
        temp += dfs(count+1, visited | (1 << i), left+weights[i], right)
        if left >= right+weights[i]:
            temp += dfs(count+1, visited | (1 << i), left, right+weights[i])
              
 
    dp[visited][left] = temp
    return dp[visited][left]
      
  
T = int(input())
  
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
      
    dp = [{} for _ in range(2**N)]
      
    answer = dfs(0, 0, 0, 0)
    print(f'#{tc} {answer}')
# 계단오르기

N = int(input()) # 계단의 개수 

stairs = []
for i in range(N):
    a = int(input())
    stairs.append(a)

dp = [0]*(N+1) # 메모장 (dp 테이블)

# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
# dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

# 초기값과예외처리
dp[1] = stairs[1]
if N>=2:
    dp[2] = stairs[1] + stairs[2]
    # N이 2보다 클 때만 dp[3] 등을 계산하도록 설계 

# 3번 계단부터 N번까지 순서대로 계산 
for i in range(3,N+1):
    # 현재(i) 도착 = i-1은 안밟음 

    case1 = dp[i-2] + stairs[i]

    case2 = dp[i-3] + stairs[i-1] + stairs[i] # i-2 건너뜀 

    dp[i]=max(case1,case2)  # 두 방법 중 더 큰 점수에 메모장에 기록 


print(dp[N])
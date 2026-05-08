import sys
input = sys.stdin.readline

# DP : 큰 문제를 작은 문제들의 합으로 쪼개어 해결
# 각 계단에 도착했을 떄 얻을 수 있는 최대 점수를 계속해서 기록

# 조건 (한번에 1계단 OR 2계단/연속된 세 개의 계단X/마지막 도착 계단 반드시)
# DP[i] : i번째 계단에 도착했을 때의 최댓값
# i == 마지막이라면, (i-1)을 밟고 온 경우, (i-1)을 밟지 않은 경우로 나뉨
# (i-1) 밟은 경우 : (i-2)번 절대 밟으면 x : (i-3) -> (i-1) -> i순으로
#즉, DP[i-3] + 계단[i-1] + 계단[i]

# (i-1) 밟지 않은 경우 = (i-2)을 밟고 옴 = (i-2) -> i 순서로
# 즉, DP[i-2] + 계단[i]

# 최종 점화식 : DP[i] = max(DP[i-3] + 계단[i-1], DP[i-2]) + 계단[i]
# *점화식 : 수열에서 이웃하는 항들 사이의 관계를 나타낸 식
# 현재 단계의 정답을 구하기 위해 이전 단계의 정답들을 어떻게 조합해야 하는가?

## stairs = 각 계단에 적혀 있는 점수 !! 

def STAIR():
    N = int(input())
    stairs = [0] * 301
    for i in range(1, N+1):
        stairs[i] = int(input()) # 각 계단에 적힌거 입력받기 

    # DP 테이블 초기화 (i번째 계단까지 최댓값 저장)
    DP = [0] * 301

    # 초기값 설정
    # N이 1이나 2일 떄를 대비해 설정
    DP[1] = stairs[1]
    if N >= 2:
        DP[2] = stairs[1] + stairs[2]
    if N >= 3:
# 3번째 계단부터 신경써야함
        DP[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])
# 4번째 계단부터 마지막 N번째 계단까지 계산
    for i in range(4,N+1):
        DP[i] = max(DP[i-3] + stairs[i-1],DP[i-2]) + stairs[i]
    print(DP[N])


STAIR()
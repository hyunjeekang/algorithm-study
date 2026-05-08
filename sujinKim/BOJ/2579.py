import sys
sys.stdin = open("input.txt")

N = int(input())
stairs = [0]*301 # 계단 최대 300개
arr = []
for i in range(1,N+1):
    stairs[i] = int(input())
    # A = int(input())
    # arr.append(A)

# 근데 뽑는것의 갯수가 적혀있는건 아니고
# 규칙대로 계단을 올랐을 때, 총 점수의 최댓값

# 계단이 N개 있어... 근데 무조건 N은 밟아야하고

# 상황 1 : N-2를 밟고 N밟기
# 상황 2: N-1를 밟고 N밟기 -> 그 전에 N-3에서 왔어야함
# 중간에 K,K+1,K+2 이렇게 연속 안됨
# 근데 이걸 내가 어캐 아노


# DP = [0] * (계단수 +1) == 리스트
# DP[i] == i번째 계단에 도달했을 때 얻을 수 있는 최대 점수

# DP 테이블 만들기 
DP = [0] * 301

# 초기값 
DP[1] = stairs[1]

if n >= 2:
if n >= 3:
    
    
# 점화식

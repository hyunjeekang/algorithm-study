# 26408 긴급수리원
# N*N크기의 구역 / M대의 고장 기계 , M명의 의뢰인 
# 기계 양수, 의뢰인 음수 
dr = [-1,1,0,0]  # 상하좌우 
dc = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input.split())) for _ in range(N)]

    for i in range(
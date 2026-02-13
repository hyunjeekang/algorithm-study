#오목판정

dr = [0,1,1,1]  # 오른쪽아래 오른쪽 위 
dc = [1,0,1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    for r in range(N):
        for c in range(N):


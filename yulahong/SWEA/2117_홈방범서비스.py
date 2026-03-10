# 가로세로 N 그리드
# K = 한 변의 길이?
# 마름모 모양
# 운영비용 = K * K + (K - 1) * (K - 1)
# 도시 벗어나도 운영비용 변경되지 않음
# M = 홈방범 서비스 지불 비용
# 손해를 보지 않으면서 가장 많이 제공할 수 있는 서비스 영역과 제공받는 집들의 수 출력
 
 
# 필요한 변수
# 지도 
 
T = int(input())
 
for tc in range(1, T+1):
     
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # 지도
    ans = 0
    home_lst = []
    for r in range(N): # 집 좌표 저장하기 위해 돌기
        for c in range(N):
            if arr[r][c] == 1:
                home_lst.append((r,c))
 
    for r in range(N): # 마름모 안에 임의의 점 정해줄거임
        for c in range(N):
            for k in range(1, N+2): # 마름모 모양을 결정지을 K를 1부터 늘려볼거임
 
                cnt = 0
                for cr, cc in home_lst: #내가 구한 집 좌표
                    dist = abs(r - cr) + abs(c - cc) #맨해튼 거리공식 한수 배웠습니다.
                    if dist <= k - 1: # 안에 있으면
                        cnt += 1 # 카운트 갱신
 
                cost = k * k + (k - 1) * (k - 1) #운영비용
                if cnt * M >= cost: # 수익이 운영비용보다 같거나 크면
                    ans = max(ans, cnt) # 더 큰걸로 갱신
 
    print(f'#{tc} {ans}')
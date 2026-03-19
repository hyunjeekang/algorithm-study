T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    chargers = set(map(int, input().split())) 
    
    cnt = 0
    cur = 0 # 현재 위치
    
    while cur + k < n: # 목적지에 도달할 때까지 반복
        # 현재 위치에서 최대 이동 거리(k)부터 거꾸로 1칸씩 줄이며 탐색
        for step in range(cur + k, cur, -1):
            if step in chargers:
                cur = step # 충전소가 있으면 이동
                cnt += 1
                break
        else:
            # for문에서 break가 걸리지 않았다면 = 충전소를 못 찾았다면
            cnt = 0
            break
            
    print(f"#{test_case} {cnt}")
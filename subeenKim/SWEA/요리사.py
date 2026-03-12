T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N//2
    food_all = [i for i in range(N)]
    values = [list(map(int, input().split())) for _ in range(N)]
    # 1은 무조건 selected 그룹에 넣는다. 그럼 {1,2,3},{4,5,6}과 {4,5,6},{1,2,3}을 같은 것으로 취급 가능
    comb = []
    for target in range(1 << N):
        # 1번 원소 (인덱스 0)를 선택했고, 개수가 N//2개이면 찾기
        if not (target & 1): # 1번 원소가 0이면 skip
            continue

        cnt = 0
        for i in range(N): # 1이면 카운트 값 증가
            if (target >> i) & 1:
                cnt += 1

        if cnt == n:
            selected = [food_all[i] for i in range(N) if (target >> i) & 1]
            unselected = [food_all[i] for i in range(N) if not ((target >> i) & 1)]
            comb.append([selected, unselected])

    min_synergy = float('inf')
    for g1, g2 in comb:
        g1_synergy, g2_synergy = 0, 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                g1_synergy += values[g1[i]][g1[j]]
                g2_synergy += values[g2[i]][g2[j]]
        diff = abs(g1_synergy - g2_synergy)
        min_synergy = diff if diff < min_synergy else min_synergy
    
    print(f'#{tc} {min_synergy}')
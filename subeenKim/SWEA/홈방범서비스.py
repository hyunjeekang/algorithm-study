# 처음 접근 : 각 집을 중심점으로 두고 다른 집까지의 거리를 구해둔 다음
# k를ㄹ 1씩 늘리면서 그 안에 들어오는 집 개수를 세서 계산하면 되지 않을까?
# 하지만 놓치는 경우 생김! > 격자의 모든 칸을 중심점으로 두고 계산!

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    grid = list(list(map(int, input().split())) for _ in range(N))
    answer = 0

    houses = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                houses.append((i, j))

    for r in range(N):
        for c in range(N):
            dist = [0]*(2*N)
            for hx, hy in houses:
                dist[abs(r-hx) + abs(c-hy)] += 1
            
            house_cnt = 0
            for k in range(1, 2*N):
                house_cnt += dist[k-1]
                cost = k*k + (k-1)*(k-1)

                if (house_cnt*M - cost) >= 0:
                    answer = max(answer, house_cnt)
        
    print(f'#{tc} {answer}')
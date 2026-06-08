def calc_honeys(M, x, y):
    max_honeys = 0
    for i in range(1<<M):
        total = 0
        got_honeys = 0
        for j in range(M):
            if (i & (1 << j)) :
                total += grid[x][y+j]
                if total > C : break
                got_honeys += (grid[x][y+j])*(grid[x][y+j])
        else:
            if got_honeys > max_honeys :
                max_honeys = got_honeys
    return max_honeys

for tc in range(1, 1+int(input())):
    N, M, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    honey = [[0]*(N-M+1) for _ in range(N)]

    # 각 칸별 채취할 수 있는 꿀의 양 계산하기
    for x in range(N):
        for y in range(N-M+1):
            honey[x][y] = calc_honeys(M, x, y)
    
    # 겹치지 않게 두 군데 구하기
    # 같은 줄에서 2개 고르는 경우
    max_case1 = 0
    for x in range(N):
        for y in range(N-2*M):
            total = honey[x][y] + max(honey[x][y+M:])
            if total >= max_case1:
                max_case1 = total
    # 다른 줄에서 하나씩 고르는 경우
    max_values = []
    for x in range(N):
        max_values.append(max(honey[x]))
    max_case2 = sum(sorted(max_values)[-2:])
    print(f'#{tc} {max(max_case1, max_case2)}')
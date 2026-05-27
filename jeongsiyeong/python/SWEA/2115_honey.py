def get_max_profit(honey_list, C):
    max_profit = 0
    M = len(honey_list)

    for i in range(1 << M):
        current_sum = 0
        current_profit = 0

        for j in range(M):
            if i & (1<<j):
                current_sum += honey_list[j]
                current_profit += honey_list[j] ** 2
        if current_sum <= C:
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit

T = int(input())

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())

    bee_house = [list(map(int, input().split())) for _ in range(N)]

    combinations = []
    ans = 0
    for r1 in range(N):
        for c1 in range(N):
            for r2 in range(r1, N):
                if r1 == r2:
                    start_c2 = c1 + M
                else:
                    start_c2=0
                for c2 in range(start_c2, N-M + 1):
                    worker_A = bee_house[r1][c1: c1+M]
                    worker_B = bee_house[r2][c2: c2+M]

                    profit_A = get_max_profit(worker_A, C)
                    profit_B = get_max_profit(worker_B, C)

                    ans = max(ans, profit_A + profit_B)


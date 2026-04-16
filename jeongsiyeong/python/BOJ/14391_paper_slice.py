N, M = map(int, input().split())

grid = [list(map(int, list(input()))) for _ in range(N)]

max_sum = 0

for mask in range(1<<(N*M)):
    cur_sum = 0
    
    # row 방향 합 계산하기
    for r in range(N):
        row_sum = 0
        for c in range(M):
            idx = r * M + c
            #0을 만나면 더해주기
            if ((mask & (1<<idx)) == 0):
                row_sum = row_sum * 10 + grid[r][c]
            else:
                #아니면 끊어주기 새로운 조각
                cur_sum += row_sum
                row_sum = 0
        cur_sum += row_sum
        
    for c in range(M):
        col_sum = 0
        for r in range(N):
            idx = r * M + c
            if ((mask & (1<<idx)) != 0):
                col_sum = col_sum * 10 + grid[r][c]
            else:
                cur_sum += col_sum
                col_sum = 0
        cur_sum += col_sum
    
    max_sum = max(max_sum, cur_sum)

print(max_sum)
# combination
def get_valid_set(arr): 
    valid_set = []
    curr_set = []
    def comb(idx,curr_sum):
        if curr_sum > C: # prunning
            return
        if idx == M:
            valid_set.append(curr_set[:]) # shallow copy
            return
        curr_set.append(arr[idx])
        comb(idx+1, curr_sum+arr[idx])
        curr_set.pop()
        
        comb(idx+1, curr_sum)
    comb(0,0)
    return valid_set

# 꿀의 가치를 계산해주는 함수
def profit(arr):
    profit = 0
    for i in arr:
        profit += i*i
    return profit 
        
# 완전탐색  문제 
T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    grid  = [list(map(int,input().split())) for _ in range(N)]
    record = [[0]*N for _ in range(N)] # visited 
    max_total = 0
    # recording
    for i in range(N):
        for j in range(N-M+1):
            candidate = grid[i][j: j+M] # slicing 
            valid = get_valid_set(candidate)
                     
            max_val = 0
            for set in valid:
                max_val = max(max_val, profit(set))
            record[i][j] = max_val
    
    for i in range(N):
        for j in range(N-M+1):
            profitA = record[i][j]
            
            for j2 in range(j+M, N-M+1):
                profitB = record[i][j2]
                max_total = max(max_total, profitA + profitB)

            for i2 in range(i+1, N):
                for j2 in range(N-M+1):
                    profitB = record[i2][j2]
                    max_total = max(max_total, profitA + profitB)
    print(f'#{tc}',max_total)


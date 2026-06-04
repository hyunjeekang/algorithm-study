
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
    choosen = [[False]*N for _ in range(N)] # visited 
    
    max_total = 0
    
    for i in range(N):
        for j in range(N-M+1):
            candidateA = grid[i][j: j+M] # slicing 
            validA = get_valid_set(candidateA)
            
            max_A = 0
            for set in validA:
                max_A = max(max_A, profit(set))
                
            # 같은 줄의 있는경우 
            for j2 in range(j+M, N-M+1):
                candidateB = grid[i][j2:j2+M]
                validB = get_valid_set(candidateB)
                
                max_B = 0
                for set in validB:
                    max_B = max(max_B, profit(set))

                max_total = max(max_total, max_A + max_B)
            
            # 다른 줄에 있는경우(A보다 무조건 밑의줄에 존재)
            for i2 in range(i+1, N):
                for j2 in range(N-M+1):
                    candidateB = grid[i2][j2: j2+M]
                    validB = get_valid_set(candidateB)
                    
                    max_B = 0
                    for set in validB:
                        max_B = max(max_B, profit(set))

                    max_total = max(max_total, max_A + max_B)
    print(f'#{tc}',max_total)
        
                    
                    
                
            
            
            

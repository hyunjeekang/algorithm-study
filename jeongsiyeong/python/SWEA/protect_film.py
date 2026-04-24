from copy import deepcopy
T = int(input())

def passed():
    global K
    if K == 1:
        return True
    for row in range(W):
        continual = 1
        is_passed = False
        for c in range(1,D):
            if tmp_cells[c][row] == tmp_cells[c-1][row]:
                continual += 1
                if continual >= K:
                    is_passed = True
            else:
                continual = 1
        if not is_passed:
            return False
    return True
          

for test_case in range(1, T+1):
    #두께, 가로, 합격기준
    D, W, K = map(int, input().split())
    
    cells = [list(map(int, input().split())) for _ in range(D)]
    answer = float('inf')
    #모든 바꾸는 셀의 경우의 수
    for mask in range(1 << D):
        changed_col = []
        for bit in range(D):
            #바꿀 막이면
            if (mask & (1 << bit)) != 0:
                changed_col.append(bit)
        col_len = len(changed_col)
        
        if col_len >= answer:
            continue
        
        for real_mask in range(1 << col_len):
            tmp_cells = deepcopy(cells)
        
            for col_idx in range(col_len):
                if (real_mask & (1 << col_idx)) != 0:
                    b = 1
                else:
                    b = 0
                tmp_col = [b] * W
                tmp_cells[changed_col[col_idx]] = tmp_col               
            if passed():
                answer = min(answer, col_len)
    print(f'#{test_case} {answer}')
from itertools import permutations
from copy import deepcopy

def rotate(board, r, c, s):
    r,c = r-1, c-1
    
    for layer in range(s, 0, -1):
        top_r, top_c = r-layer, c-layer
        bottom_r, bottom_c = r+layer, c+layer
        
        temp = board[top_r][top_c]
        
        for i in range(top_r, bottom_r):
            board[i][top_c] = board[i+1][top_c]
        
        for i in range(top_c, bottom_c):
            board[bottom_r][i] = board[bottom_r][i+1]
        
        for i in range(bottom_r, top_r, -1):
            board[i][bottom_c] = board[i-1][bottom_c]
        
        for i in range(bottom_c, top_c+1, -1):
            board[top_r][i] = board[top_r][i-1]
        
        board[top_r][top_c+1] = temp 

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ops = [list(map(int, input().split())) for _ in range(K)]

ans = float('inf')

for p in permutations(ops):
    temp_arr = deepcopy(arr)
    
    for r,c, s in p:
        rotate(temp_arr, r, c, s)
    
    for row in temp_arr:
        ans = min(ans, sum(row))
print(ans)
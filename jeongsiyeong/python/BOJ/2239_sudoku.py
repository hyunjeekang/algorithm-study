def check_horizontal(r,c, val):
    for dc in range(9):
        if val == arr[r][dc]:
            return False
    return True

def check_vertical(r,c, val):
    for dr in range(9):
        if val == arr[dr][c]:
            return False
    return True

def check_box(r,c, val):
    start_r = (r // 3) * 3
    start_c = (c // 3) * 3
    for dr in range(3):
        for dc in range(3):
            if val == arr[start_r+dr][start_c+dc]:
                return False
    return True

def dfs(depth):
    if depth == len(blanks):
        for row in arr:
            print("".join(map(str,row)))
        exit(0)
    
    r, c = blanks[depth]
    
    for val in range(1, 10):
        if check_horizontal(r, c, val) and check_vertical(r, c, val) and check_box(r, c, val):
            arr[r][c] = val
            dfs(depth+1)
            arr[r][c] = 0

arr = [list(map(int, list(input()))) for _ in range(9)]
blanks = []
for r in range(9):
    for c in range(9):
        if arr[r][c] == 0:
            blanks.append((r,c))
            
dfs(0)
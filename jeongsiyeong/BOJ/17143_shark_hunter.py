import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    return 0 <= r < R and 0 <= c < C

R, C, M = map(int, input().split())

arr = [[-1] * C for _ in range(R)]
sharks = [(-1, -1, -1, -1, -1)] * M

for i in range(M):
    rr, cc, s, d, z = map(int, input().split())
    rr -= 1
    cc -= 1
    
    if d == 1:
        dir = 3
    elif d == 2:
        dir = 1
    elif d == 3:
        dir = 0
    else:
        dir = 2
        
    sharks[i] = (rr, cc, s, dir, z)
    arr[rr][cc] = i

total_catch = 0 

for fish_c in range(C):
    
    for r in range(R):
        if arr[r][fish_c] != -1: 
            shark_idx = arr[r][fish_c]
            total_catch += sharks[shark_idx][4] 
            
            sharks[shark_idx] = (-1, -1, -1, -1, -1) 
            arr[r][fish_c] = -1
            break 
            
    new_arr = [[-1] * C for _ in range(R)]
    
    for i in range(M):
        s_r, s_c, s_s, dir, s_z = sharks[i]
        
        if s_r == -1:
            continue
            
        if dir == 1 or dir == 3: 
            move_count = s_s % (2 * (R - 1))
        else:                
            move_count = s_s % (2 * (C - 1))
            
        for _ in range(move_count):
            nr, nc = s_r + dr[dir], s_c + dc[dir]
            
            if not is_range(nr, nc): 
                dir = (dir + 2) % 4 
                nr, nc = s_r + dr[dir], s_c + dc[dir] 
                
            s_r, s_c = nr, nc 
            
        if new_arr[s_r][s_c] == -1:
            new_arr[s_r][s_c] = i
            sharks[i] = (s_r, s_c, s_s, dir, s_z)
        else:
            existing_idx = new_arr[s_r][s_c]
            existing_z = sharks[existing_idx][4]
            
            if s_z > existing_z: 
                sharks[existing_idx] = (-1, -1, -1, -1, -1) 
                new_arr[s_r][s_c] = i 
                sharks[i] = (s_r, s_c, s_s, dir, s_z) 
            else: 
                sharks[i] = (-1, -1, -1, -1, -1) 
                
    arr = new_arr

print(total_catch)
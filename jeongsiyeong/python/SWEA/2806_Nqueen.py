def n_queen(col, ld, rd):
    global total
    global check
    
    if col == check:
        total += 1
        return
    
    valid_position = check & ~(col | ld | rd)
    
    while valid_position != 0:
        pos = valid_position & -valid_position
        
        valid_position -= pos
        
        n_queen(col|pos, (ld|pos) << 1, (rd|pos) >> 1)
    

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    half = N // 2
    total = 0
    check = (1<<N) - 1
    
    for i in range(half):
        pos = 1 << i
        n_queen(pos, pos<<1 , pos >> 1)
    
    total *= 2
    
    if N%2 == 1:
        pos = 1 << half
        n_queen(pos, pos<<1, pos>>1)
    
    print(f'#{test_case} {total}')
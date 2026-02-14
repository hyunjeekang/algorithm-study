N = int(input())

check = (1<<N) - 1
total = 0

def n_queen(col, ld, rd):
    global total

    if col == check:
        total += 1
        return
        
    valid_positions = check & (~(col | ld | rd))

    while valid_positions != 0 :
        pos = valid_positions & -valid_positions
        valid_positions -= pos

        n_queen(col|pos , (ld|pos) << 1, (rd|pos) >> 1)

half = N //2
for i in range(half):
    pos = 1 << i
    n_queen(pos, pos<<1, pos >> 1)
    
total *=2

if N%2 == 1:
    pos = 1 << half
    n_queen(pos, pos<<1, pos>>1)
    
print(total)
def get_value(r, c):
    layer = max(abs(r), abs(c))
    max_val = (2 * layer + 1) ** 2
    
    if r == layer:         
        return max_val - (layer - c)
    elif c == -layer:      
        return max_val - 2 * layer - (layer - r)
    elif r == -layer:       
        return max_val - 4 * layer - (c + layer)
    else:                   
        return max_val - 6 * layer - (r + layer)


r1, c1, r2, c2 = map(int, input().split())

board = []
max_len = 0

for r in range(r1, r2 + 1):
    row = []
    for c in range(c1, c2 + 1):
        val = get_value(r, c)
        row.append(val)
        max_len = max(max_len, len(str(val)))
    board.append(row)

for row in board:
    for val in row:
        print(f"{val:{max_len}d}", end=" ")
    print()
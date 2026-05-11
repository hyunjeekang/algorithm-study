T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def is_range(x, y):
    return -2000 <= x <= 2000 and -2000 <= y <= 2000

for test_case in range(1, T+1):
    N = int(input())

    atoms = []

    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append((2*x, 2*y, d, k)) 
    
    total = 0

    while atoms:
        nxt_atoms = []
        pos_dict = {}

        for atom in atoms:
            x, y, d, k = atom
            x += dx[d]
            y += dy[d]

            if is_range(x, y):
                if (x, y) not in pos_dict:
                    pos_dict[(x, y)] = []
                pos_dict[(x, y)].append((d, k))

        for pos, atom_list in pos_dict.items():
            if len(atom_list) > 1:
                for d, k in atom_list:
                    total += k
            elif len(atom_list) == 1:
                x, y = pos
                d, k = atom_list[0]
                nxt_atoms.append((x, y, d, k))
                
        atoms = nxt_atoms
        
    print(f'#{test_case} {total}')
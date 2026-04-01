from itertools import permutations
from itertools import product
from collections import deque
boards = []

dr = [1, 0, -1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def rotate(board):
    return list(map(list, zip(*board[::-1])))

def list_to_bitmask(board_2d):
    bit_board = []
    for r in range(5):
        row_val = 0
        for c in range(5):
            if board_2d[r][c] == 1:
                row_val |= (1<<c)
        bit_board.append(row_val)
    return bit_board

rotated_boards = [[[] for _ in range(4)] for _ in range(5)]

for b in range(5):
    board = [list(map(int, input().split())) for _ in range(5)]
    
    current_board = board
    for r in range(4):
        rotated_boards[b][r] = list_to_bitmask(current_board)
        current_board = rotate(current_board)
    boards.append(board)


def bfs(tmp_maze):
    q = deque([(0, 0, 0)])
    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0
    
    while q:
        cur_z, cur_r, cur_c = q.popleft()
        
        if cur_z==4 and cur_r==4 and cur_c == 4:
            return visited[cur_z][cur_r][cur_c]
        
        for i in range(6):
            nz = cur_z + dz[i]
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            
            if 0<=nz<5 and 0<=nr<5 and 0<=nc<5 and visited[nz][nr][nc] == -1 and (tmp_maze[nz][nr] & (1<<nc)) != 0:
                visited[nz][nr][nc] = visited[cur_z][cur_r][cur_c] + 1
                q.append((nz, nr, nc))
    return float('inf')

answer = float('inf')

for indices in permutations(range(5)):
    for rotations in product(range(4), repeat=5):
        maze = []
        
        for idx, rot in zip(indices, rotations):
            maze.append(rotated_boards[idx][rot])
            
        if not (maze[0][0] & (1<<0)) or not (maze[4][4] & (1<<4)):
            continue
        cur_ans = bfs(maze)
        
        if cur_ans < answer:
            answer = cur_ans
            if answer == 12:
                print(answer)
                exit()

if answer == float('inf'):
    print(-1)
else:
    print(answer)
        
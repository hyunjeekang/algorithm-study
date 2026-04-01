from collections import deque

N, T = map(int, input().split())
signals = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(N)]

dr = [0, 1, 0, -1] 
dc = [1, 0, -1, 0]

signs = {
    1: (0, 11), 2: (3, 13), 3: (2, 14), 4: (1, 7), 
    5: (0, 9),  6: (3, 12), 7: (2, 6),  8: (1, 3), 
    9: (0, 3), 10: (3, 9), 11: (2, 12), 12: (1, 6)
}

q = deque([(0, 0, 3, 0)])

visited_states = set()
visited_states.add((0, 0, 3, 0))

unique_cells = set()
unique_cells.add((0, 0))

while q:
    cur_r, cur_c, cur_dir, cur_time = q.popleft()
    
    if cur_time == T:
        continue

    sig_id = signals[cur_r][cur_c][cur_time % 4]
    req_dir, allowed_dirs = signs[sig_id]

    if cur_dir == req_dir:
        for i in range(4):
            if allowed_dirs & (1 << i):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                
                if 0 <= nr < N and 0 <= nc < N:
                    unique_cells.add((nr, nc)) 
                    
                    new_state = (nr, nc, i, (cur_time + 1) % 4)
                    if new_state not in visited_states:
                        visited_states.add(new_state)
                        q.append((nr, nc, i, cur_time + 1))

print(len(unique_cells))
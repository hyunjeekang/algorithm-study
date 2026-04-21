from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


dir_map = {1: 0, 2: 2, 3: 1, 4: 3}

start_r, start_c, s_d = map(int, input().split())
end_r, end_c, e_d = map(int, input().split())

start_node = (start_r-1, start_c-1, dir_map[s_d])
end_node = (end_r-1, end_c-1, dir_map[e_d])

visited = [[[-1] * 4 for _ in range(M)] for _ in range(N)]

q = deque([start_node])
visited[start_node[0]][start_node[1]][start_node[2]] = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while q:
    cur_r, cur_c, cur_dir = q.popleft()

    if (cur_r, cur_c, cur_dir) == end_node:
        print(visited[cur_r][cur_c][cur_dir])
        break

    for jump in range(1, 4):
        nr, nc = cur_r + dr[cur_dir] * jump, cur_c + dc[cur_dir] * jump

        if not (0 <= nr < N and 0 <= nc < M) or grid[nr][nc] == 1:
            break
        
        if visited[nr][nc][cur_dir] == -1:
            visited[nr][nc][cur_dir] = visited[cur_r][cur_c][cur_dir] + 1
            q.append((nr, nc, cur_dir))

    for rotation in [1, 3]:
        n_dir = (cur_dir + rotation) % 4
        if visited[cur_r][cur_c][n_dir] == -1:
            visited[cur_r][cur_c][n_dir] = visited[cur_r][cur_c][cur_dir] + 1
            q.append((cur_r, cur_c, n_dir))
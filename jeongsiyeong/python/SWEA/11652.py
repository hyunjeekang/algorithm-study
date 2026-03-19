from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = []
    start_r, start_c = 0, 0
    end_r, end_c = 0, 0

    for r in range(N):
        line = input()
        row_list = [int(ch) for ch in line]
        arr.append(row_list)
        
        for c in range(N):
            if row_list[c] == 2:
                start_r, start_c = r, c
            elif row_list[c] == 3:
                end_r, end_c = r, c

    ans = 0
    q = deque()
    q.append((start_r, start_c, 0)) 

    visited = [[False] * N for _ in range(N)]
    visited[start_r][start_c] = True

    def is_range(r, c):
        return 0 <= r < N and 0 <= c < N

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while q:
        curr_r, curr_c, cur_dist = q.popleft()

        if curr_r == end_r and curr_c == end_c:
            ans = cur_dist - 1 
            break

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if is_range(nr, nc):
                if arr[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, cur_dist + 1))

    print(f'#{test_case} {ans}')
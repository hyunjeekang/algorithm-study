T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    global R, C
    return 0<=r<R and 0<=c<C

def dfs(cur_r, cur_c):
    global answer
    answer = max(answer, len(alpha_set))
    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]

        if is_range(nr, nc) and not visited[nr][nc]:
            if grid[nr][nc] not in alpha_set:
                alpha_set.add(grid[nr][nc])
                visited[nr][nc] = True

                dfs(nr, nc)

                visited[nr][nc] = False
                alpha_set.remove(grid[nr][nc])
        

for test_case in range(1, T+1):
    R, C = map(int, input().split())

    grid = [list(input()) for _ in range(R)]

    alpha_set = set()
    visited = [[False] * C for _ in range(R)]

    alpha_set.add(grid[0][0])
    visited[0][0] = True
    answer = 0
    dfs(0, 0)

    print(f'#{test_case} {answer}')
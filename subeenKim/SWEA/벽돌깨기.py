from collections import deque

def break_bricks(y, next_grid):
    start_r = -1
    for i in range(H):
        if next_grid[i][y] > 0:
            start_r = i
            break
    if start_r == -1:
        return 0
    q = deque([(start_r, y, next_grid[start_r][y])])
    next_grid[start_r][y] = 0
    total_cnt = 1
    while q:
        r, c, power = q.popleft()
        if power <= 1:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r, c
            for _ in range(power - 1):
                nr, nc = nr+dr, nc+dc
                if (0 <= nr < H and 0 <= nc < W):
                    if next_grid[nr][nc] > 0:
                        q.append((nr, nc, next_grid[nr][nc]))
                        next_grid[nr][nc] = 0
                        total_cnt += 1
                else:
                    break

    for w in range(W):
        point = H-1
        for h in range(H-1, -1, -1):
            if next_grid[h][w] > 0:
                if point != h:
                    next_grid[point][w] = next_grid[h][w]
                    next_grid[h][w] = 0
                point -= 1
    return total_cnt


def backtrack(current_grid, cnt, broken):
    global max_broken

    max_broken = max(broken, max_broken)

    # 종료조건
    if broken == total_bricks or cnt == N:
        return
    
    # 벽돌을 터뜨릴 위치 선정
    for c in range(W):
        # 복사
        next_grid = [row[:] for row in current_grid]
        # 터뜨리고, 떨어뜨리기
        new_broken = break_bricks(c, next_grid)
        if new_broken == 0 :
            continue
        # 백트래킹
        backtrack(next_grid, cnt+1, broken + new_broken)
    


for tc in range(1, 1+int(input())):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    total_bricks = 0
    for y in range(W):
        for x in range(H):
            if grid[x][y] > 0 :
                total_bricks += 1
    max_broken = 0
    backtrack(grid, 0, 0)
    print(f'#{tc} {total_bricks - max_broken}')
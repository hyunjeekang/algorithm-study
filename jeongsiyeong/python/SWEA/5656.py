from collections import deque
#벽돌 깨기
T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # 1. 재귀를 이용한 중복 순열 구현
    # 2. 블록이 연쇄적으로 파괴되는 함수 구현
    # 3. 공백 0으로 채우는 함수 구현
    # 4. 남은 블록 수 세는 함수 구현
    result = float('inf')
    def copy_arr(src):
        return [row[:] for row in src]
    def count_blocks(src):
        cnt = 0
        for r in range(H):
            for c in range(W):
                if src[r][c] != 0:
                    cnt += 1
        return cnt
    def drop_blocks(src):
        for c in range(W):
            stack = []
            for r in range(H-1, -1, -1):
                if src[r][c] != 0:
                    stack.append(src[r][c])
            for r in range(H-1, -1, -1):
                if stack:
                    src[r][c] = stack.pop(0)
                else:
                    src[r][c] = 0
    def break_blocks(src, col):
        q = deque()
        for r in range(H):
            if src[r][col] != 0:
                q.append((r, col, src[r][col]))
                break
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r, c, power = q.popleft()
            src[r][c] = 0
            for d in directions:
                nr, nc = r, c
                for _ in range(power - 1):
                    nr += d[0]
                    nc += d[1]
                    if 0 <= nr < H and 0 <= nc < W and src[nr][nc] != 0:
                        if src[nr][nc] > 1:
                            q.append((nr, nc, src[nr][nc]))
                        src[nr][nc] = 0
    def dfs(depth, src):
        global result
        if depth == N:
            remaining = count_blocks(src)
            result = min(result, remaining)
            return
        for c in range(W):
            new_arr = copy_arr(src)
            break_blocks(new_arr, c)
            drop_blocks(new_arr)
            dfs(depth + 1, new_arr)
    dfs(0, arr)
    print(f"#{test_case} {result}")
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def is_range(r,c):
        return 0<=r<N and 0<=c<N
    #가로세로
    d1r = [0, 1, 0, -1]
    d1c = [1, 0, -1, 0]
    #대각선
    d2r = [1, -1, -1, 1]
    d2c = [1, 1, -1, -1]
    mx_kill = 0
    for r in range(N):
        for c in range(N):
            kill1 = arr[r][c]
            for direction in range(4):
                for power in range(1,M):
                    nr = r + d1r[direction] * power
                    nc = c + d1c[direction] * power
                    if is_range(nr, nc):
                        kill1 += arr[nr][nc]
            mx_kill = max(mx_kill, kill1)
            kill2 = arr[r][c]
            for direction in range(4):
                for power in range(1,M):
                    nr = r + d2r[direction] * power
                    nc = c + d2c[direction] * power
                    if is_range(nr, nc):
                        kill2 += arr[nr][nc]
            mx_kill = max(mx_kill, kill2)
    print(f'#{test_case} {mx_kill}')          
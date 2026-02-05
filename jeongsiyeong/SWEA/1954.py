#1954 달팽이
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
     
    # 방향 벡터: 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
     
    r, c = 0, 0  # 시작 위치
    direction = 0  # 초기 방향: 우
    for num in range(1, N * N + 1):
        snail[r][c] = num
         
        # 다음 위치 계산
        nr = r + dr[direction]
        nc = c + dc[direction]
         
        # 경계 체크 및 이미 채워진 칸 체크
        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            direction = (direction + 1) % 4  # 방향 전환
            nr = r + dr[direction]
            nc = c + dc[direction]
         
        r, c = nr, nc  # 다음 위치로 이동
     
    print(f"#{test_case}")
    for row in snail:
        print(' '.join(map(str, row)))
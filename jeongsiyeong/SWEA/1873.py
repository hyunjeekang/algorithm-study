#상호의 배틀 필드
# . 평지(전차가 들어갈 수 있다)
# * 벽돌로 만들어진 벽
# # 강철로 만들어진 벽
# - 물(전차는 들어갈 수 없다)
# ^ 위쪽을 바라보는 전차(아래는 평지이다)
# V 아래쪽을 바라보는 전차(아래는 평지이다)
# < 왼쪽을 바라보는 전차(아래는 평지이다)
# > 오른쪽을 바라보는 전차(아래는 평지이다)

# 입력 종류
# U Up: 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D Down: 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L Left: 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R Right: 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

#벽돌로 만들어진 벽 포탄 부딪히면 평지

T = int(input())

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    def is_range(r,c):
        return 0<=r<H and 0<=c<W
    arr = [list(input()) for _ in range(H)]

    fortress = [0, 0, 0 ] # r, c, dir
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for r in range(H):
        for c in range(W):
            if arr[r][c] == '>':
                fortress[0] = r
                fortress[1] = c
                fortress[2] = 0
                break
            elif arr[r][c] == 'V':
                fortress[0] = r
                fortress[1] = c
                fortress[2] = 1
                break
            elif arr[r][c] == '<':
                fortress[0] = r
                fortress[1] = c
                fortress[2] = 2
                break
            elif arr[r][c] == '^':
                fortress[0] = r
                fortress[1] = c
                fortress[2] = 3
                break
    
    N = int(input())
    cmds = input()
    for cmd in cmds:
        if cmd == 'U':
            fortress[2] = 3
            arr[fortress[0]][fortress[1]] = '^'
            nr = fortress[0] + dr[fortress[2]]
            nc = fortress[1] + dc[fortress[2]]
            if is_range(nr,nc) and arr[nr][nc] == '.':
                arr[fortress[0]][fortress[1]] = '.'
                fortress[0] = nr
                fortress[1] = nc
        elif cmd == 'D':
            fortress[2] = 1
            arr[fortress[0]][fortress[1]] = 'V'
            nr = fortress[0] + dr[fortress[2]]
            nc = fortress[1] + dc[fortress[2]]
            if is_range(nr,nc) and arr[nr][nc] == '.':
                arr[fortress[0]][fortress[1]] = '.'
                fortress[0] = nr
                fortress[1] = nc
        elif cmd == 'L':
            fortress[2] = 2
            arr[fortress[0]][fortress[1]] = '<'
            nr = fortress[0] + dr[fortress[2]]
            nc = fortress[1] + dc[fortress[2]]
            if is_range(nr,nc) and arr[nr][nc] == '.':
                arr[fortress[0]][fortress[1]] = '.'
                fortress[0] = nr
                fortress[1] = nc
        elif cmd == 'R':
            fortress[2] = 0
            arr[fortress[0]][fortress[1]] = '>'
            nr = fortress[0] + dr[fortress[2]]
            nc = fortress[1] + dc[fortress[2]]
            if is_range(nr,nc) and arr[nr][nc] == '.':
                arr[fortress[0]][fortress[1]] = '.'
                fortress[0] = nr
                fortress[1] = nc
        elif cmd == 'S':
            # 포탄 발사
            sr, sc = fortress[0], fortress[1]
            while True:
                sr += dr[fortress[2]]
                sc += dc[fortress[2]]
                if not is_range(sr, sc) or arr[sr][sc] == '#': # 맵 밖이나 강철 벽
                    break
                if arr[sr][sc] == '*': # 벽돌 벽
                    arr[sr][sc] = '.'
                    break
    
    print(f'#{test_case}',end=" ")
    for line in arr:
        print("".join(line))
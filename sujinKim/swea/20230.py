#풍선팡 보너스게임2

dr = [0,1,0,-1] #우하좌상
dc = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max = 0
    #기준점 (r,c) 먼저 정한다.
    for r in range(N):
        for c in range(N):
            p = arr[r][c]

            for dir in range(4):
                for i in range(1,N):
                    nr = r + dr[dir]*i
                    nc = c + dc[dir]*i

                    if 0 <= nr < N and 0 <= nc < N:
                        p += arr[nr][nc]


            if p > max:
                max = p

    print(f'#{tc} {max}')








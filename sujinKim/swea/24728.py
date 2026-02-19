dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    total_max = 0
    for r in range(N):
        for c in range(N):
            cur_r, cur_c = r,c #현재 위치 
            count = 1
            # p = arr[cur_r][cur_c]
            # min_h = p

            while True:
                p = arr[cur_r][cur_c]
                min_h = p
                n_r,n_c = -1,-1


                for i in range(4): # 상하좌우로 움직이기 가능 
                    nr = cur_r +dr[i]
                    nc = cur_c +dc[i]
                    # q = arr[nr][nc]

                    if 0 <= nr < N and 0 <=nc<N:
                        if arr[nr][nc] < min_h:
                            min_h = arr[nr][nc]
                            n_r,n_c = nr,nc
                if n_r != -1:
                    cur_r,cur_c = n_r,n_c
                    count += 1
                else:
                    break 



                # while True:
                #     if min_h > q:
                #         cur_r, cur_c = nr, nc 
                #         count += 1

                #     else:
                #         break 

            if count > total_max:
                total_max = count 

    print(f'#{tc} {total_max}')
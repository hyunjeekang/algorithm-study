T = int(input())
#우 하 좌 상
dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]

dir_map = {1 : 3, 2:1 , 3 : 2 ,4 : 0}

for test_case in range(1, T+1):
    #셀 개수, 격리 시간, 미생물 군집 수
    N, M, K = map(int, input().split())
    
    bios = []
    for _ in range(K):
        r, c, bio_cnt, dir = map(int, input().split())
        
        bios.append((r, c, bio_cnt, dir_map[dir]))
    
    for turn in range(M):
        for bio_idx in range(K):
            r, c, cnt, dir = bios[bio_idx]
            if cnt != 0:
                nr = r + dr[dir]
                nc = c + dc[dir]
                if nr == 0 or nr == N-1 or nc ==0 or nc ==N-1:
                    cnt = cnt //2
                    dir = (dir+2) % 4
                bios[bio_idx] = (nr, nc, cnt, dir)
        bios.sort(key= lambda x: (x[0], x[1], -x[2]))
        for bio_idx in range(K):
            r, c, cnt, dir = bios[bio_idx]
            if cnt != 0:
                for n_bio in range(bio_idx+1, K):
                    pr, pc, p_cnt, p_dir = bios[n_bio]
                    if r == pr and c == pc:
                        if cnt > p_cnt:
                            cnt += p_cnt
                            p_cnt = 0
                        else:
                            p_cnt += cnt
                            cnt = 0
                        bios[n_bio] = (pr, pc, p_cnt, p_dir)
                        bios[bio_idx] = (r, c, cnt, dir)
    total_bio = 0
    for bio_idx in range(K):
        r, c, cnt, dir = bios[bio_idx]
        total_bio += cnt
    print(f'#{test_case} {total_bio}')

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
cctvs = []

for r in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    for c in range(M):
        if 1 <= line[c] <= 5:
            cctvs.append((r, c, line[c]))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 상(0), 우(1), 하(2), 좌(3)
# 비트값: 상(1), 우(2), 하(4), 좌(8)
cctv_bits = [0, 1, 5, 3, 11, 15]

cctv_cnt = len(cctvs)
min_spot = N * M

for i in range(1 << (2 * cctv_cnt)):
    temp_arr = [line[:] for line in arr]

    for j in range(cctv_cnt):
        r, c, c_type = cctvs[j]

        # j번째 cctv의 방향값 (0~3) 추출
        dir = (i >> (2 * j)) & 3
        
        cur_bit = cctv_bits[c_type]

        for k in range(4):
            if (cur_bit >> k) & 1:
                dir_idx = (k + dir) % 4

                nr, nc = r, c
                
                # [수정 1] while문 로직 변경
                while True:
                    nr += dr[dir_idx]
                    nc += dc[dir_idx]
                    
                    # 이동한 좌표가 범위를 벗어나거나 벽(6)이면 break
                    if not (0 <= nr < N and 0 <= nc < M) or temp_arr[nr][nc] == 6:
                        break
                    
                    # 빈 칸이면 감시 영역 표시
                    if temp_arr[nr][nc] == 0:
                        temp_arr[nr][nc] = 7

    cnt = 0
    for rr in range(N):
        # [수정 2] r -> rr 로 변경
        cnt += temp_arr[rr].count(0) 

    if cnt < min_spot:
        min_spot = cnt

print(min_spot)
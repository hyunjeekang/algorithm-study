dr = [0, 1, 1, 1]   # 오른쪽, 아래, 우하대각, 좌하대각
dc = [1, 0, 1, -1]

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    found = False   # ⭐ 여기서 한 번만 선언
    for r in range(N):
        # if found: #
        #     break  #
        for c in range(N):
            # if found: 
            #     break #

            if arr[r][c] == 'o':

                for dir in range(4):
                    p = 1

                    for i in range(1, 5):
                        nr = r + dr[dir] * i
                        nc = c + dc[dir] * i

                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                p += 1
                            else: #
                                break #
                        else: #
                            break #

                    if p >= 5:
                        found = True
                        break

    if found:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

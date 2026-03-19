import sys
from collections import deque

input = sys.stdin.readline # 입력 속도 향상

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
air_c = []
for r in range(R):
    if arr[r][0] == -1:
        air_c.append((r, 0))

# 우, 하, 좌, 상 (문제의 dr, dc 순서 유지)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r,c):
    return 0 <= r < R and 0 <= c < C

for _ in range(T):
    # [수정 1] dust 리스트는 매 턴마다 새로 구해야 함
    dust = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0: # -1(청정기) 제외
                dust.append((r, c))

    # [수정 2] 동시 확산을 위해 변화량을 저장할 배열 생성
    diff = [[0] * C for _ in range(R)]
    
    for r, c in dust:
        if arr[r][c] < 5: continue # 5 미만은 확산 안 됨
        moving_dust = arr[r][c] // 5
        cnt = 0
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # [수정 3] nr, nc 계산을 for문 안으로 넣음 (기존엔 밖에 있었음)
            if is_range(nr, nc) and arr[nr][nc] != -1:
                diff[nr][nc] += moving_dust
                cnt += 1
        
        diff[r][c] -= moving_dust * cnt

    # 확산 적용 (원본 배열 + 변화량)
    for r in range(R):
        for c in range(C):
            arr[r][c] += diff[r][c]

    # 공기청정기 작동
    for i in range(2):
        cir_r, cir_c = air_c[i]
        
        d_list = []
        path_coords = [] # 좌표를 기억해둘 리스트
        
        direction = 0 # '우' 부터 시작
        nr, nc = cir_r, cir_c + 1 # 청정기 바로 다음 칸부터 시작
        
        # 한 바퀴 돌아서 다시 원점으로 올 때까지 반복
        while not (nr == cir_r and nc == cir_c):
            d_list.append(arr[nr][nc])
            path_coords.append((nr, nc))
            
            # 다음 이동할 좌표 계산
            next_r = nr + dr[direction]
            next_c = nc + dc[direction]
            
            # 맵을 벗어나면 방향 전환
            if not is_range(next_r, next_c):
                # [수정된 부분] i=0이면 -1(반시계), i=1이면 +1(시계)
                if i == 0:
                    direction = (direction - 1) % 4
                else:
                    direction = (direction + 1) % 4
                    
                nr += dr[direction]
                nc += dc[direction]
            else:
                nr = next_r
                nc = next_c

        # 바람 이동 (0 추가, 마지막 제거)
        d_list.insert(0, 0)
        d_list.pop()
        
        # 값 다시 채워넣기
        for idx, (r, c) in enumerate(path_coords):
            arr[r][c] = d_list[idx]

# 정답 출력
ans = 0
for row in arr:
    ans += sum(row)
print(ans + 2) # 공기청정기 값(-1 두 개) 보정
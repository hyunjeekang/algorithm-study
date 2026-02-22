dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global answer

    visited[r][c] = 1
    # 4방향 탐색 
    # - 인덱스 범위 안쪽 and 방문하지 X and 0임(해당 인덱스에 접근해야 알 수 있는 값들)
    # dir : 델타의 인덱스
    for dir in range(4):
        nr = r+dr[dir]
        nc = c+dc[dir]
        # 갈 수 있음
        # - 인덱스 범위 안쪽 and 방문하지 X and 1이 아님(해당 인덱스에 접근해야 알 수 있는 값들)
        # if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0 and arr[nr][nc] != 1:
        
        # 갈 수 없음
        # - 인덱스 범위 바깥 or 방문했음 or 1임(해당 인덱스에 접근해야 알 수 있는 값들)
        # 인덱스 밖
        if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
            continue
        # 방문 했거나 벽이면
        if visited[nr][nc] == 1 or arr[nr][nc] == 1:
            continue
        if arr[nr][nc] == 3:
            answer = 1
            return

        dfs(nr, nc)

# 5 +1
# 10 +1
# 15 +1
# if a >= 5:
#     b += 1
# if a >= 10:
#     b += 1

# students = [
#     ['김영원', 30, '강사'],
#     ['홍유라', 27, '교육생'],
# ]

# for student in students:
#     # 이름 가지고 제어
#     if student[0] 
    
#     # 나이 가지고 제어
#     if student[1]

    


T = 10
for tc in range(1, T+1):

    answer = 0
    input()
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    # 미로 도는 함수 정의 > 끝점을 발견하면 answer를 1로 바꾸는 기능

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_r = i
                start_c = j
            elif arr[i][j] == 3:
                goal_r = i
                goal_c = j
    
    dfs(start_r, start_c)


    print(f'#{tc} {answer}')
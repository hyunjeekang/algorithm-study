#미생물 격리
#정사각형 구역 안에 K개의 미생물 군집이 존재
#가장 바깥쪽 가장자리 부분 셀들 특수한 약품 칠해짐
#미생물 군집 위치, 미생물 수, 이동 방향 주어짐
#각 군집은 1시간에 1칸씩 이동
#격리 구역의 가장자리 부분 셀에 도달하면 미생물 수
#절반으로 줄어들고, 이동 방향은 반대 방향으로 바뀜
#미생물 수가 홀수인 경우, 절반으로 줄인 후 소수점 이하 버림
#두 개 이상의 군집이 한 셀에 모이게 되면
#하나의 군집으로 합쳐지며, 미생물 수가 가장 많은 군집의 이동 방향을 따름
#M시간 동안 미생물 군집 이동시킨 후 남아있는 미생물 수의 총합 구하기

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i][0] = -1
        arr[i][N-1] = -1
        arr[0][i] = -1
        arr[N-1][i] = -1
    microbes = []
    for _ in range(K):
        r, c, num, direction = map(int, input().split())
        microbes.append([r,c,num,direction])
    # 방향: 1:up, 2:down, 3:left, 4:right
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    for _ in range(M):
        for microbe in microbes:
            r, c, num, direction = microbe
            nr = r + dr[direction-1]
            nc = c + dc[direction-1]
            microbe[0], microbe[1] = nr, nc
            if arr[nr][nc] == -1:
                microbe[2] //= 2
                if microbe[2] == 0:
                    microbe[3] = 0
                else:
                    if direction == 1:
                        microbe[3] = 2
                    elif direction == 2:
                        microbe[3] = 1
                    elif direction == 3:
                        microbe[3] = 4
                    elif direction == 4:
                        microbe[3] = 3
        temp = dict()
        for microbe in microbes:
            r, c, num, direction = microbe
            if num == 0:
                continue
            if (r,c) in temp:
                temp[(r,c)].append((num,direction))
            else:
                temp[(r,c)] = [(num,direction)]
        new_microbes = []
        for key in temp:
            r, c = key
            group = temp[key]
            if len(group) == 1:
                num, direction = group[0]
                new_microbes.append([r,c,num,direction])
            else:
                group.sort(reverse=True)
                total_num = sum([g[0] for g in group])
                direction = group[0][1]
                new_microbes.append([r,c,total_num,direction])
        microbes = new_microbes
    result = sum([microbe[2] for microbe in microbes])
    print(f"#{test_case} {result}")
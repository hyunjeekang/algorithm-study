import heapq
 
def hit(a, b): # a번 원자와 b번 원자 충돌하는 경우 정리
    x1, y1, d1, _ = atom[a]
    x2, y2, d2, _ = atom[b]
    time = float('inf')
    # case1 : x 좌표가 같고, 서로를 보는 방향으로 움직임 (방향이 각각 0, 1 > 합이 무조건 1)
    if (x1 == x2) and (d1 + d2 == 1):
        if (y2 > y1 and d2 == 1) or (y1 > y2 and d1 == 1):
            time = (max(y1, y2) - min(y1, y2))/2
    # case2 : y 좌표가 같고, 서로를 보는 방향으로 움직임 (방향이 각각 2, 3 > 합이 무조건 5)
    elif (y1 == y2) and (d1 + d2 == 5):
        if (x2 > x1 and d2 == 2) or (x1 > x2 and d1 == 2):
            time = (max(x1, x2) - min(x1, x2))/2
    # case3 : x좌표 차이 == -y좌표 차이 (두 점을 이은 기울기가 -1) (방향이 각각 1, 2 또는 0, 3 > 합이 3)
    elif ((x1 - x2) == -(y1 - y2)) and (d1 + d2 == 3):
        if (x1 - x2) > 0 and (d1 == 2 or d1 == 0): # x1 > x2
            time = x1 - x2
        elif (x1 - x2) < 0 and (d1 == 1 or d1 == 3) : # x1 < x2
            time = x2 - x1
    # case4 : x좌표 차이 == y좌표 차이 (두 점을 이은 기울기가 1) (방향이 각각 0, 2 또는 1, 3 > 차가 2)
    elif ((x1 - x2) == (y1 - y2)) and (d1 - d2 == 2 or d1 - d2 == -2):
        if (x1 - x2) > 0 and (d1 == 2 or d1 == 1): # x1 > x2
            time = x1 - x2
        elif (x1 - x2) < 0 and (d1 == 0 or d1 == 3) : # x1 < x2
            time = x2 - x1
    return time
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    alive_atom = [True]*N
    bombs = []
 
    for a in range(N-1): # 모든 부딪힐 수 있는 경우를 담아 bombs에 저장
        for b in range(a+1, N):
            time = hit(a, b)
            if time != float('inf'):
                heapq.heappush(bombs, (time, a, b))

    # 가장 충돌 시간이 빠른것부터 소멸시키기!
    # 충돌 시간이 같은 것끼리는 한 번에 모아서 소멸시킨다.
    # 만약 두 원자 중 하나라도 이미 사라진 원자면 pass! (충돌이 일어날 수 없기 때문)
    while bombs :
        time, a1, a2 = heapq.heappop(bombs)
        disapear = set()
        if (not alive_atom[a1]) or (not alive_atom[a2]):
            continue
        disapear.add(a1)
        disapear.add(a2)
        while bombs and (bombs[0][0] == time) :
            time, n1, n2 = heapq.heappop(bombs)
            if (not alive_atom[n1]) or (not alive_atom[n2]):
                continue
            disapear.add(n1)
            disapear.add(n2)
        for d in disapear :
            alive_atom[d] = False

    # alive_atom 에 충돌했으면 값이 false로 바뀌어져 있음. false인 것만 모아서 합 구하기
    answer = sum(atom[i][3] for i in range(N) if not alive_atom[i])
    print(f'#{tc} {answer}')
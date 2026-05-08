from collections import deque

def go_down_stairs(stair, num):
    time = 0
    if len(stair) > 0:
        s = deque([stair[0]])
        sidx = 1 # 가장 먼저 도착한 사람은 이미 큐에 넣었기 때문에 0이 아닌 1부터 시작
        slength = stairs[num][2] # 계단 길이
        time = s[0]-1 # 시작하자마자 time+1 할거기 때문에 미리 1 빼줌
        while (sidx < len(stair)) or s: # 계단에 아무도 남아있지 않고, 이 계단으로 온 사람이 다 이동할 때까지 반복
            time += 1
            # 계단에 사람이 있고, 이동 완료 시 빼주기
            while s and (s[0] + slength <= time):
                s.popleft()
            # 새로운 사람 넣기 / 아직 도착한 사람이 없으면 pass
            while (sidx < len(stair)) and (time >= stair[sidx]) and (len(s) < 3):
                s.append(max(time, stair[sidx]))
                sidx += 1
    return time

T = int(input())
for tc in range(1, T+1):
    answer = float('inf')
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    people, stairs, = [], []
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 1:
                people.append((x, y))
            elif grid[x][y] > 1:
                stairs.append((x, y, grid[x][y]))

    n = len(people)
    distance = []
    for p in range(n): # count of people
        # distance의 p번째에 p번 사람이 [계단01로 이동하는 경우, 계단2로 이동하는 경우]의 이동 거리(대기시간 1 포함)
        distance.append([abs(people[p][0] - stairs[0][0]) + abs(people[p][1] - stairs[0][1]) + 1, abs(people[p][0] - stairs[1][0]) + abs(people[p][1] - stairs[1][1]) + 1])

    # 사람이 4명이라고 하면 0000, 0001, 0010, ... , 1110, 1111 까지 모든 경우를 탐색하며 완전탐색을 한다.
    for i in range(1 << n):
        stair0, stair1 = [], []
        for j in range(n):
            # j번째 사람의 i & (1<<j) 한 결과가 0이 나오면 계단 0을 선택함 / 그렇지 않으면 계단 1을 선택한 것
            idx = i & (1<<j)
            if idx == 0:
                stair0.append(distance[j][0])
            else:
                stair1.append(distance[j][1])
        # 계단 내려가기 시작 / 정렬해서 먼저 도착한 사람부터 계단으로 이동할 수 있도록 함
        stair0.sort()
        stair1.sort()
        time0 = go_down_stairs(stair0, 0)
        time1 = go_down_stairs(stair1, 1)
        # 계단 0, 1 중에 더 오래 걸린 것이 총 이동 시간이 됨
        total = max(time0, time1)
        answer = min(total, answer)

    print(f'#{tc} {answer}')
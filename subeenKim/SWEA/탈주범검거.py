import sys; sys.stdin = open('sample_input.txt')

from collections import deque

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 1) 연결되어 있는 지하 터널 찾기
    # 상 우 하 좌 순으로 했을 때 연결될 수 있는 터널 구조물 타입
    cango = [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]]
    # N번 터널 구조물이 다른 구조물과 연결될 수 있는 방향
    connected_dir = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]
    # 이동 가능한 칸을 나타내자!
    grid = [[0]*M for _ in range(N)]
    grid[R][C] = 1

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([(R, C)])
    while q :
        x, y = q.popleft()
        for d in connected_dir[data[x][y]]:
            nx, ny = x+dir[d][0], y+dir[d][1]
            if (0 <= nx < N and 0 <= ny < M) and (grid[nx][ny] == 0):
                if data[nx][ny] in cango[d]:
                    q.append((nx, ny))
                    grid[nx][ny] = 1

    # 2) 이동할 수 있는 곳 개수 구하기
    visited = [[False]*M for _ in range(N)]
    location = deque([(R, C, 1)])
    visited[R][C] = True
    answer = 1
    while location:
        x, y, cnt = location.popleft()
        if cnt >= L:
            continue
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if (0 <= nx < N and 0 <= ny < M)  and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    location.append((nx, ny, cnt+1))
                    visited[nx][ny] = True
                    answer += 1
    
    print(f'#{tc} {answer}')
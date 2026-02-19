from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 3종류의 폭탄이 터졌을 때 각각 초토화되는 지역
bomb = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], 
    [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)], 
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]]

# 각 폭탄별로 폭탄 종류 - 중복 가능, 순서 있음 (0 -> 1번 폭탄, 1 -> 2번 폭탄, 2 -> 3번 폭탄)
def bomb_kind(temp_list):
    if len(temp_list) == bomb_cnt:
        cases.append(temp_list[:])
        return
    for i in range(3):
        temp_list.append(i)
        bomb_kind(temp_list)
        temp_list.pop()

# 폭탄이 놓이는 위치 모으기
bomb_loc = []
bomb_loc = deque([])
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_loc.append((i, j))
bomb_cnt = len(bomb_loc)

cases = []
bomb_kind([])
max_cnt = 0
for case in cases:
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for k in range(bomb_cnt):
        x, y = bomb_loc[k]
        for dx, dy in bomb[case[k]]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] :
                    cnt += 1
                    visited[nx][ny] = True
    max_cnt = cnt if cnt > max_cnt else max_cnt
print(max_cnt)
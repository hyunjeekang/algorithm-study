n = int(input())
grid = [list(input()) for _ in range(n)]

def backtrack(start, temp_list):
    if len(temp_list) == 3:
        method.append(temp_list[:])
        return
    
    for i in range(start, len(coins)):
        temp_list.append(coins[i])
        backtrack(i+1, temp_list)
        temp_list.pop()

# 시작점, 끝점, 동전 좌표 찾아서 저장
coin_dict = {}
for x in range(n):
    for y in range(n):
        if grid[x][y] == 'S':
            sx, sy = x, y
        elif grid[x][y] == 'E':
            fx, fy = x, y
        elif '0' <= grid[x][y] <= '9':
            coin_dict[int(grid[x][y])] = (x, y)

# 코인의 종류를 찾아서 오름차순 정렬
coins = sorted(list(coin_dict.keys()))

# 코인 개수가 최소 3개가 안되면 -1 출력하고 끝
if len(coins) < 3 :
    print(-1)
else :
    method = []
    backtrack(0, [])

    min_cnt = float('inf')
    # 거리 계산
    for met in method :
        cnt = 0
        for i in range(2):
            x1, y1 = coin_dict[met[i]]
            x2, y2 = coin_dict[met[i+1]]
            cnt += (abs(x2 - x1) + abs(y2 - y1))
            if i == 0 :
                cnt += (abs(sx - x1) + abs(sy - y1))
            if i == 1 :
                cnt += (abs(fx - x2) + abs(fy - y2))
        # 값 갱신
        min_cnt = cnt if cnt < min_cnt else min_cnt

    print(min_cnt)
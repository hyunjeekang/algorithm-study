n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def get_gold_num(row, col, k, n, grid):
    cnt = 0
    # 맨해튼 거리 계산
    for i in range(n):
        for j in range(n):
            distance = abs(row - i) + abs(col-j)
    
            if distance <= k :
                cnt += grid[i][j]
    return cnt

max_gold = 0

# k개의 인접한 마름모 (중앙과 거리가 k 이하)
for k in range(n+1):
    # 모든 격자에 대해서 탐색
    for x in range(n):
        for y in range(n):
            current_gold = get_gold_num(x, y, k, n, grid)

            # 손해를 보지 않으면
            if current_gold*m - (k*k + (k+1)*(k+1)) >= 0 :
                max_gold = current_gold if current_gold > max_gold else max_gold

print(max_gold)
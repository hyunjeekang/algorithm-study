n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

def backtrack(idx, total, hap):
    global max_weight
    if hap > c:
        return

    if idx == m:
        max_weight = max(total, max_weight)
        return
    
    for i in range(idx,m):
        # 선택
        backtrack(idx+1, total + weight[x][y+idx]**2, hap + weight[x][y+idx])
        # 선택 X
        backtrack(idx+1, total, hap)

grid = [[0]*(n-m+1) for _ in range(n)]
for x in range(n):
    for y in range(n-m+1):
        max_weight = 0
        backtrack(0, 0, 0)
        grid[x][y] = max_weight

# 한 줄에서 2개 선택
same_max = 0
for x in range(n):
    for y in range(n-m+1 - m):
        for k in range(y+m, n-m+1):
            hap = grid[x][y] + grid[x][k]
            same_max = hap if hap > same_max else same_max

# 다른 줄에서 1개씩 선택
max1, max2 = 0, 0
for x in range(n):
    line_max = max(grid[x])
    if line_max > max1:
        max1, max2 = line_max, max1
    elif line_max > max2:
        max2 = line_max
other_max = max1 + max2

print(max(same_max, other_max))
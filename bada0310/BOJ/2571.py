# https://www.acmicpc.net/problem/2571
# 히스토드램에서 가장 큰 사각형 찾기 
# 다시 풀어봐야할것
N = int(input())
grid = [[0]*100 for _ in range(100)]

for _ in range(N):
    r, c = map(int,input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            grid[i][j] = 1
        
heights = [[0] * 100 for _ in range(100)]
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            if i == 0:
                heights[i][j] = 1
            else:
                heights[i][j] = heights[i-1][j] + 1
        else:
            heights[i][j] = 0

max_area = 0
for i in range(100):
    for j in range(100):
        h = 100
        for k in range(j, 100):
            h = min(h, heights[i][k])
            
        if h == 0:
            break
        
        curr_area = (k -j +1) *h
        max_area = max(max_area, curr_area)
print(max_area)

    

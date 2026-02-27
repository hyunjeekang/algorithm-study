from collections import deque
N, M = map(int,input().split()) # N grid M 치킨집 수 
grid = [list(map(int,input().split())) for _ in range(N)] 

arr = []
house = []
for x in range(N):
    for y in range(N):
        if grid[x][y] == 2:
            arr.append((x, y))
        if grid[x][y] == 1:
            house.append((x,y))

chicken = []
path = []
def comb(start, M): # m
    # 기저 조건
    if len(path) == M:
        chicken.append(path[:])
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        comb(i + 1, M)
        path.pop()
comb(0,M)

min_city_val = float('inf')

for row in chicken:
    city_val = 0
    for h_r , h_c in house:
        min_house_val = float('inf')
        for c_r, c_c in row:
            dist = (abs(h_r - c_r)+ abs(h_c - c_c))
            if dist < min_house_val:
                min_house_val = dist
        city_val += min_house_val
    if min_city_val > city_val:
        min_city_val = city_val
print(min_city_val)

        










































# min_dist = 0
# dir = [(0, 1),(1,0),(-1,0),(0, -1)]
# chicken = []
# for i in range(M): # 치킨집에 대해서 
#     for x in range(N):
#         for y in range(N):
#             if grid[x][y] == 1:
#                 start = (x, y)
#                 min_dist += bfs(start,N,grid)

# # 집을 찾아  그리고 각 2 까지의 거리를 구해 > 비교해 > 가장 짧으 거리를 구해 > dist 더해 


# # def bfs(start,N,grid):
# #     x, y = start[0], start[1]
# #     q = deque() 
# #     q.append(start[0],start[1]) # 초기값 
# #     visited = [[False]*N for _ in range(N)]
# #     visited[start[0], start[1]] = True

# #     dir = [(0, 1), (1,0), (-1,0), (0,-1)]
# #     for dx, dy in dir:
# #         nx, ny = x + dx , y + dy
# #         if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 2 and not visited[nx][ny]:
# #             visited[nx][ny] = 0
# #             dist = abs(nx-x)+abs(ny-y)
# #     return dist
            
 
    
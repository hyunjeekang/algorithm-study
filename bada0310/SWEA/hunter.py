N = int(input())
grid= [list(map(int,input().split())) for _ in range(N)]
arr = []
mon = []
human = []
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            if grid[i][j] > 0:
                human.append(grid[i][j])
                mon.append(grid[i][j])
            arr.append(grid[i][j])

# 순열
# dr dc 로 탐색 
path = [] # 개별 순열을 담을 공간
# go = [] # 조건에 부합하는 순열을 담을 공간
visited =[False]*(len(arr))
min_val = float('inf')
def perm(start):
    global min_val
    # 기저 조건 
    if len(path) == len(arr):
        # 최소거리 구하기 
        dist = 0 # 거리 
        curr_x, curr_y = 0, 0 # 초기값 
        for i in range(len(path)):
            for x in range(N):
                for y in range(N):
                    if grid[x][y] == path[i]:
                        dist += (abs(curr_x-x)+ abs(curr_y-y))
                        curr_x, curr_y = x, y
            if dist < min_val:
                min_val = dist
        return 
    for i in range(len(arr)):
        if not visited[i] and -arr[i] in path:
            visited[arr[i]] =True
            path.append(arr[i])

            perm(start+1)
            visited[arr[i]]=False
            path.pop()
perm(0)


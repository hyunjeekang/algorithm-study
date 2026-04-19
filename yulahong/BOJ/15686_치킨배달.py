# # bfs로 풀다가 망함.....
# 치킨거리 = 집과 가까운 치킨집 사이의 거리, 집을 기준으로 정해짐
# 도시의 치킨 거리 = 모든 치킨거리의 합
# 지금 치킨 집 중 m개를 뽑을거임


n, m = map(int, input().split())
house = []
chicken = []
min_dist = 1e9


for r in range(n):
    row = list(map(int, input().split()))
    for c in range(n):
        if row[c] == 1: # 집 찾으면 집 리스트에 넣기
            house.append((r, c))
        elif row[c] == 2: # 치킨 집 찾으면 치킨집 리스트에 넣기
            chicken.append((r, c))

# 한 집마다의 치킨거리를 lst에 저장
# lst = []
# 전체 말고 선택된 것만 받아서 치킨거리 반환하기
# def cal(i):
#     lst = []
#     for i in len(house):
#         for j in len(chicken):
#             dist = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
#             lst.append(dist)

def cal(path):
    total_city_dist = 0
    for hr, hc in house:
        # 이 집에서 가장 가까운 치킨집까지의 거리 찾기
        d_min = 1e9
        for idx in path:
            cr, cc = chicken[idx]
            dist = abs(hr - cr) + abs(hc - cc)
            d_min = min(d_min, dist)
        total_city_dist += d_min
    return total_city_dist

# 치킨리스트에 대한 조합 함수
visited = [0]*len(chicken)
path = []
def recur(cnt, prev):
    global visited
    global min_dist
    global m
    if cnt == m:
        result = cal(path)
        min_dist = min(min_dist, result)
        return
        
    
    for i in range(prev, len(chicken)):
        if visited[i] == 1:
            continue

        path.append(i)
        visited[i] = 1
        recur(cnt + 1, i +1)
        path.pop()
        visited[i] = 0


recur(0, 0)
print(int(min_dist))




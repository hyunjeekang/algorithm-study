# bfs로 풀다가 망함.....


n, m = map(int, input().split())
house = []
chicken = []

for r in range(n):
    row = list(map(int, input().split()))
    for c in range(n):
        if row[c] == 1: # 집 찾으면 집 리스트에 넣기
            house.append((r, c))
        elif row[c] == 2: # 치킨 집 찾으면 치킨집 리스트에 넣기
            chicken.append((r, c))

min_city_dist = 999999  # 충분히 큰 값으로 초기화


selected = []

def get_dist():
    total = 0
    for hr, hc in house:
        temp_min = 999999
        for idx in selected:
            cr, cc = chicken[idx]
            # 맨해튼 거리 계산
            dist = abs(hr - cr) + abs(hc - cc)
            if dist < temp_min:
                temp_min = dist
        total += temp_min
    return total

# 조합 
def solve(start, count):
    global min_city_dist
    
    # M개를 골랐을 때 최솟값 갱신
    if count == m:
        min_city_dist = min(min_city_dist, get_dist())
        return

    for i in range(start, len(chicken)):
        selected.append(i)
        solve(i + 1, count + 1)
        selected.pop()  # 다음 경우의 수를 위해 마지막 선택 취소

# 실행
solve(0, 0)
print(min_city_dist)
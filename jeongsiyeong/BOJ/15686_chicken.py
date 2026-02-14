N, M = map(int, input().split())

houses = []
stores = []

arr = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            houses.append((r,c))
        elif arr[r][c] == 2:
            stores.append((r,c))

ans =float('inf')

for m in range(1<<len(stores)):
    if bin(m).count('1') == M:
        part_stores = []
        for i in range(len(stores)):
            if m & (1<<i) :
                part_stores.append(stores[i])

        city_dist = 0

        for h_r, h_c in houses:
            sub_dist = float('inf')

            for s_r, s_c in part_stores:
                dist = abs(h_r - s_r) + abs(h_c - s_c)
                sub_dist = min(dist, sub_dist)
            city_dist += sub_dist
        ans = min(ans, city_dist)
print(ans)
            
        
# 1번부터 n번까지 n개의 정점과 m개의 간선에 대한 정보로, 
# 간선의 양 끝 정점과 해당 간선의 가중치가 주어짐. 
# 최소 스패닝 트리를 구하는 프로그램 작성하기

# 그래프의 모든 정점을 연결하는 부분 그래프 중에서, 
# 그 가중치의 합이 최소가 되는 부분그래프를 의미

# 인접행렬을 이용하여 O(N^2)에 프림 알고리즘 구현


# n,m = map(int,input().split())  # n개의 정점, m개의 간선 
# for i in range(m):

import sys
INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n,m = tuple(map(int,input().split()))
graph = [
    [0] * (n+1)
    for _ in range(n+1)
]
visited = [False] * (n+1)

# 그래프에 있는 모든 노드들에 대해 
# 초기값을 전부 아주 큰 값으로 설정 
dist = [INT_MAX] * (n+1)

# 그래프를 인접행렬로 표현
for _ in range(m):
    x,y,z = tuple(map(int,input().split()))
    graph[x][y] = z if graph[x][y] == 0 else min(graph[x][y],z)
    graph[y][x] = z if graph[y][x] == 0 else min(graph[y][x],z)

# 시작위치에는 dist값을 0으로 설정 
dist[1] = 0

# 0(|V|^2) 프림 코드 
ans = 0
for i in range(1,n+1):
    # V개의 정점 중
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아준다. 
    min_index = -1
    for j in range(1,n+1):
        if visited[j]:
            continue

        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j
    # 최솟값에 해당하는 정점에 방문 표시를 진행한다. 
    visited[min_index] = True

    # mst 값을 갱신해준다. 
    ans += dist[min_index]

    # 최소값에 해당하는 정점에 연결된 간선들을 보며.......
    # 시작점으로부터의 최솟값을 갱신해준다....
    for j in range(1,n+1):
        # 간선이 존재하지 않는 경우에는 넘어간다.........
        if graph[min_index][j] == 0:
            continue

        dist[j] = min(dist[j],graph[min_index][j])

print(ans)

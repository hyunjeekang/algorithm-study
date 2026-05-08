# 각 정점까지의 최단 경로 3
# N개의 정점이 존재하고 M개의 간선의 양 끝 정점과 가중치가 주어질 때,
# 1번 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 프로그램을 작성해봐라 
# 이때 주어지는 정점과 간선들로 구성되는 그래프는 단방향 그래프라고 가정 

# N,M = map(int,input().split())  # 정점의 개수 : N , 간선의 개수 : M
# for i in range(M): # M개의 줄에 걸쳐, 각 간선의 시작 정점의 번호, 끝 정점의 번호, 그리고 해당 간선에 주어진 가중치가 공백을 두고 주어진다.

# 다익스트라는 특정 시작점에서 다른 모든 정점으로 가는 최단거리를 각각 구해주는 알고리즘이다. 
import sys
INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n,m = tuple(map(int,input().split()))
graph = [
    [0]*(n+1)
    for _ in range(n+1)
]
visited = [False]*(n+1)

# 그래프에 있는 모든 노드들에 대해 
# 초기값을 전부 아주 큰 값으로 설정 

dist = [INT_MAX]*(n+1)

# 그래프를 인접행렬로 표현 
for _ in range(m):
    x,y,z = tuple(map(int,input().split()))
    graph[x][y] = z

# 시작위치에는 dist값을 0으로 설정 
dist[1] = 0

for i in range(1,n+1):
    min_index = -1
    for j in range(1,n+1):
        if visited[j]:
            continue

        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j


    for j in ragne(1,n+1):
        if graph[min_index][j] == 0:
            continue

        dist[j] = min(dist[j],dist[min_index]+graph[min_index][j])

# 시작점(1번 정점)으로부터 각 지점까지의 최단거리를 값을 출력한다. 
for i in range(2,n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])


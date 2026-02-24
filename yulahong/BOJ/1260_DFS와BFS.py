# dfs결과 bfs 결과 출력 프로그램
# 방문할 수 있는 정점 여려개 > 정점 번호가 작은 것 먼저 방문
# 방문할 점 없는 경우 종료
# 간선 양방향
# 첫줄에 dfs 다음줄에 bfs 결과 출력

# 변수
# 첫줄: N = 정점의 개수, M = 간선의 개수, V = 탐색을 시작할 정점의 번호
# M개의 줄에 간선 연결하는 두 정점 번호 주어짐 > for 문으로 M번 돌기

#변수

from collections import deque
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [0] * (N+1)

def dfs(node):
    visited_dfs[node] = 1
    print (node, end = ' ')

    for i in graph[node]:
        if visited_dfs[i] == 0:
            dfs(i)

visited_bfs = [0] * (N+1)

def bfs(node):
    q = deque([node])
    visited_bfs[node] = 1

    while q :
        node = q.popleft()
        print(node, end = ' ')

        for i in graph[node]:
            if visited_bfs[i] == 0:
                q.append(i)
                visited_bfs[i] = 1
        
dfs(V)
print()
bfs(V)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

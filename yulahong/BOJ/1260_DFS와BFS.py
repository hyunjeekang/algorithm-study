# dfs결과 bfs 결과 출력 프로그램
# 방문할 수 있는 정점 여려개 > 정점 번호가 작은 것 먼저 방문
# 방문할 점 없는 경우 종료
# 간선 양방향

# 변수
# 첫줄: N = 정점의 개수, M = 간선의 개수, V = 탐색을 시작할 정점의 번호
# M개의 줄에 간선 연결하는 두 정점 번호 주어짐 > for 문으로 M번 돌기

#변수
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

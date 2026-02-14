import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, dest = map(int, input().split())

def dijkstra():

    hq = []
    dist = [float('inf')]*(N+1)
    heapq.heappush(hq, (start, 0))
    dist[start] = 0

    while hq:
        cn, cw = heapq.heappop(hq)

        # 최단거리 이미 초과 시
        if dist[cn] < cw:
            continue
        
        # 다음 경로 탐색
        for nn, w in graph[cn]:
            nw = dist[cn] + w
            # 기존 경로보다 짧은 경로면 업데이트
            if nw < dist[nn]:
                dist[nn] = nw
                heapq.heappush(hq, (nn, w)) 

    print(dist[dest])

dijkstra()
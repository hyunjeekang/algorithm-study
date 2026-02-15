import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input().strip())
graph = [[]for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra():
    hq = []
    heapq.heappush(hq, (0, start))

    dist = [float('inf')]*(V+1)
    dist[start] = 0

    while hq:
        curWeight, curNode = heapq.heappop(hq)

        if dist[curNode] < curWeight:
            continue
        
        for nextNode, weight in graph[curNode]:
            newWeight = curWeight + weight

            if newWeight < dist[nextNode]:
                dist[nextNode] = newWeight
                heapq.heappush(hq, (newWeight, nextNode))

    for i in range(1, V+1):
        if dist[i] == float('inf'):
            print('INF')
        else: print(dist[i])

dijkstra()
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())

distance = [float('inf')]*(N+1)
parent = [0] * (N+1)
distance[start] = 0
q = [(0, start)]

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next, cost in graph[now]:
        if dist + cost < distance[next]:
            distance[next] = dist + cost
            heapq.heappush(q, (distance[next], next))
            parent[next] = now

print(distance[end])
path = []
curr = end
while curr != 0:
    path.append(curr)
    curr = parent[curr]

print(len(path))
print(*path[::-1])
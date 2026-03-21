import heapq

n, m = map(int, input().split())
# 양방향이기 때문에 reverse 와 non-reverse 동일
edges = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    edges[s].append((c, e))
    edges[e].append((c, s))
A, B = map(int, input().split())

# 최단거리 구하기 (역으로 end -> start)
distance = [float('inf')]*(n+1)
distance[B] = 0
q = [(0, B)]

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for cost, nnode in edges[now]:
        new_dist = dist + cost
        if new_dist < distance[nnode]:
            distance[nnode] = new_dist
            heapq.heappush(q, (new_dist, nnode))

print(distance[A])
# 사전순 경로 찾기
# 시작점 -> 끝점 순회하며 dist[i] + graph[i][x] == dist[x] 인 정점으로 이동
path = [A]
curr = A
for edge in edges:
    edge.sort(key = lambda x: x[1])
while curr != B:
    for c, n in edges[curr]:
        if distance[n] + c == distance[curr]:
            curr = n
            path.append(curr)
            break

print(*path)
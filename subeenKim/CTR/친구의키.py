from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

# 시작점 큐에 넣기
q = deque([])
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

# 위상정렬 진행
order = []
while q:
    node = q.popleft()
    order.append(node)
    for x in edges[node]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)

print(*order)

import heapq
N, K = map(int, input().split())

pq = []
INF = float('inf')
heapq.heappush(pq, (0, N))
visited  = [INF] * (100001)
visited[N] = 0
while pq:
    cost, pos = heapq.heappop(pq)
    
    if cost > visited[pos]:
        continue
    
    if pos == K:
        break
    
    if pos*2 <= 100000:
        if cost < visited[pos * 2]:
            visited[pos * 2] = cost
            heapq.heappush(pq, (cost, pos*2))
    
    if pos + 1 <= 100000:
        if cost + 1 < visited[pos + 1]:
            visited[pos + 1] = cost + 1
            heapq.heappush(pq, (cost+1, pos+1))
    
    if pos -1 >=0:
        if cost+1 < visited[pos - 1]:
            visited[pos - 1] = cost + 1
            heapq.heappush(pq, (cost+1, pos -1))
    
print(visited[K])
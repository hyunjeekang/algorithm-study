import heapq

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int , input().split())
    
    graph = [[] for _ in range(V+1)]
    
    for edge in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    dist = [float('inf')] * (V+1)
    
    dist[0] = 0
    
    pq = [(0,0)]
    
    while pq:
        cur_weight, cur_node = heapq.heappop(pq)
        
        if cur_weight > dist[cur_node]:
            continue
                
        for next_node, weight in graph[cur_node]:
            next_weight = weight + cur_weight
            if next_weight < dist[next_node]:
                dist[next_node] = next_weight
                heapq.heappush(pq, (next_weight, next_node))
    
    print(f'#{test_case} {dist[V]}')
    
        
    
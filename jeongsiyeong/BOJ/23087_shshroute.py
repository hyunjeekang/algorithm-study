import heapq
N,M,x,y = map(int, input().split())

MOD = 10**9 + 9

graph=[[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int,input().split())
    graph[start].append((end,weight))

dijk = [float('inf')] * (N+1)
edge_cnt = [float('inf')] *(N+1)
path_cnt = [0] * (N+1)

pq = []

heapq.heappush(pq,(0,0,x))
dijk[x] = 0
edge_cnt[x] = 0
path_cnt[x] = 1


while pq:
    now_dist, now_edges, now_node = heapq.heappop(pq)
    if dijk[now_node] < now_dist or (dijk[now_node] == now_dist and edge_cnt[now_node] < now_edges):
        continue

    for n_node, n_weight in graph[now_node]:
        nxt_dist = now_dist + n_weight
        nxt_edges = now_edges + 1

        if dijk[n_node] > nxt_dist :
            dijk[n_node] = nxt_dist
            edge_cnt[n_node] = nxt_edges
            path_cnt[n_node] = path_cnt[now_node]
            heapq.heappush(pq,(nxt_dist, nxt_edges, n_node))
        
        elif dijk[n_node] == nxt_dist and edge_cnt[n_node] > nxt_edges:
            edge_cnt[n_node] = nxt_edges
            path_cnt[n_node] = path_cnt[now_node]
            heapq.heappush(pq, (nxt_dist, nxt_edges, n_node))
        
        elif dijk[n_node] == nxt_dist and edge_cnt[n_node] == nxt_edges:
            path_cnt[n_node] = (path_cnt[n_node] + path_cnt[now_node]) % MOD

if dijk[y] == float('inf'):
    print(-1)
else:
    print(dijk[y])
    print(edge_cnt[y])
    print(path_cnt[y])



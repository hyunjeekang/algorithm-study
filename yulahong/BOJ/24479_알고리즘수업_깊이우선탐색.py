N, M, S = map(int, input().split()) # 정점의 수, 간선정보, 시작 정점

adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    adj[i].sort()

def dfs(node):
    global cnt
    visited[node] = cnt

    for neighbor in adj[node]:
        cnt += 1
        if not visited[neighbor]:
            dfs(neighbor)

dfs(S)

for i in range(1, N+1):
    print(visited[i])



from collections import deque

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = {}

    for edge in range(E):
        v1, v2 = map(int, input().split())

        if v1 not in adj.keys():
            adj.setdefault(v1, [v2])
        else:
            adj[v1].append(v2)
        
        if v2 not in adj.keys():
            adj.setdefault(v2, [v1])
        else:
            adj[v2].append(v1)

    S, G = map(int, input().split())
    visited = [False] * (V+1)

    q = deque()
    q.append((S, 0))
    visited[S] = True
    ans = 0
    while q:
        cur_node, cur_dist = q.popleft()

        if cur_node == G:
            ans = cur_dist
            break

        for node in adj.get(cur_node,[]):
            if not visited[node]:
                q.append((node, cur_dist+1))
                visited[node] = True
    
    print(f'#{test_case}', ans)

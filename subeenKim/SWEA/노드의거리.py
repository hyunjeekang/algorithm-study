from collections import deque

def bfs(graph, start, visited):
    q = deque([(start, 0)])
    visited[start] = True

    while q :
        node, cnt = q.popleft()
        if node in graph:
            for n in graph[node]:
                if not visited[n] :
                    if n == G:
                        return cnt+1
                    q.append((n, cnt+1))
                    visited[n] = True

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    visited = [False]*(V+1)
    for _ in range(E):
        n, m = map(int, input().split())
        if n in graph:
            graph[n].append(m)
        else :
            graph[n] = [m]
        if m  in graph:
            graph[m].append(n)
        else :
            graph[m] = [n]

    S, G = map(int, input().split())
    answer = bfs(graph, S, visited)
    if answer :
        print(f'#{tc} {answer}')
    else :
        print(f'#{tc} 0')
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
    
    while q:
        current = q.popleft()
        if current == E:
            print(visited[current])
            return
        
        nexts = [current+1, current-1] + graph[current]
        
        for next in nexts:
            if 1<=next<=N and visited[next] == -1:
                visited[next] = visited[current] + 1 
                q.append(next)
            
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    S, E = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    
    visited = [-1] * (N+1)
    bfs(S)
        
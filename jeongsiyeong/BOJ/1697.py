from collections import deque

def bfs(start, target):
    visited = [0] * 100001

    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()

        if cur == target:
            return visited[cur]

        for nex_pos in (cur-1, cur+1, cur*2):
            if 0<=nex_pos<=100000 and not visited[nex_pos]:
                visited[nex_pos] = visited[cur] + 1
                q.append(nex_pos)
    
n, k = map(int, input().split())
print(bfs(n, k))

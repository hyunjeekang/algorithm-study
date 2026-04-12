import sys
from collections import deque
sys.stdin = open("input.txt")


input = sys.stdin.readline

def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

# 입력 처리
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬 (작은 번호부터 방문)
for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# 실행
dfs(v)
print()
bfs(v)
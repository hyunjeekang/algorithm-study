import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1  

visited = [[False] * M for _ in range(N)]
visited[0][0] = True

pq = []
heapq.heappush(pq, (-arr[0][0], 0, 0))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while pq:
    height, r, c = heapq.heappop(pq)
    
    if r == N - 1 and c == M - 1:
        continue
        
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] < arr[r][c]:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(pq, (-arr[nr][nc], nr, nc))
            
            dp[nr][nc] += dp[r][c]

print(dp[N-1][M-1])
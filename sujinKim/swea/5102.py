# 가중치가 같으니까 bfs == 최소값
import sys
sys.stdin = open("input.txt")

from collections import deque
def bfs(S,G,V,graph):
    # 이제 그래프를 돌아다니면서 값을 쓰는 함수를 만들어줄건데
    distance = [0]* (V+1) #각 노드마다 시작점-노드 거리
    visited = [False]*(V+1) # 노드를 방문했는지 안했는지

    queue = deque([S]) # 시작점을 덱에 넣어서 시작 !
    visited[S] = True # 시작점 방문처리 해줘야겠지?

    while queue:
        cur = queue.popleft() #queue에서 앞에서부터 노드 빼가지고 현재값으로 설정

        if cur == G : # 근데 만약에 꺼낸 현재 노드가 == 도착 노드랑 같다면?
            return distance[cur] # 그 현재노드(도착노드)의 거리값을 반환해라

        # 같지 않다면?
        for neighbor in graph[cur]: # graph에서 현재노드가 속하는 리스트의 이웃노드를 하나씩 꺼내봐
            if not visited[neighbor]: # 그 이웃노드가 방문하지 않았던것이라면
                visited[neighbor] = True # 우선 방문처리 해주고
                distance[neighbor] = distance[cur] + 1 # distanc의 neighbor에 distance의 cur보다 +1 해
                queue.append(neighbor) # 글고 그 이웃을 현재지점으로 만들기 위해 queue에 넣어




T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    graph = [[]for _ in range(V+1)] # 그래프의 인접리스트 만들어주고
    for _ in range(E):  #연결된 간선의 수만큼 반복
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u) # 양방향이니까 그래프에서 연결된 양쪽 차례대로 넣어주기
    S,G = map(int,input().split())  #시작노드,끝노드

    result = bfs(S,G,V,graph)
    print(f'#{tc} {result}')




import sys
import heapq
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())

    graph = [[]for _ in range(N+1)] # (도착노드,가중치) 저장

    for i in range(E):
        s,e,w = list(map(int,input().split())) # 시작노드,도착노드,가중치
        graph[s].append((e,w)) # graph에 입력받은거 저장해놔
    INF = int(1e9) # 경로의 최대합보다 큰 값 준비

    def dijkstra(start,N,graph): # 매개변수 : 시작,끝, 가중치 1개의 사용위치

        # 1. 최단 거리 테이블 초기화
        distance = [INF]*(N+1) # 각 노드마다의 최단거리 저장해두는 곳

        q = []
        # 최단 거리를 가진 노드를 빠르게 뽑아내기 위해
        # 다익스트라 알고리즘에서 앞으로 방문할 노드들을 세워두는 대기열
        # 처음에는 아무도 줄을 서 있지 않으니까 빈 리스트로

        heapq.heappush(q,(0,start)) # q에 (거리,노드)순으로 묶어서 넣어라
        # 우선 시작을 이렇게 하는거지?

        distance[start]=0

        while q:
            dist,now = heapq.heappop(q) # 저장해두었던 q의 (거리,노드)를 꺼내
            # now = 현재 노드 위치겠지?
            if distance[now] < dist : # 현재 노드 위치에 저장된 거리값이 q에서 꺼낸 dist값보다 작다면
                continue
                # 이 말은 예를 들어 now가 4면 distance[now]는 0부터 4까지의 거리합인건가?

            for next_node,weight in graph[now]: # graph의 지금 위치에 저장해둔 튜플을 하나씩 꺼내는데
                cost = dist + weight
                # 비용은 = 저장해두었던 q에서 꺼낸 비용에 + 그 다음 가중치
                if cost < distance[next_node]: # 그래서 새로운 비용이 저장해두었던 다음 노드의 비용보다 작으면
                    distance[next_node] = cost
                    heapq.heappush(q,(cost,next_node))

        return distance
    dist_result = dijkstra(0,N,graph)

    print(f'#{tc} {dist_result[N]}')




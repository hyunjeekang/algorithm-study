#루트노드가 1인 트리에서 각 노드의 부모 노드를 구하는 프로그램 
#두 번째 줄부터 N번째 줄까지 트리 상에서 연결된 두 정점이 주어진다. 
# 일반적으로 트리에 대한 정보는 두 정점간의 연결 관계만 주어지기 때문에 연결된 두 정점 중 누가 부모이고 자식인지를 알 수 없다. 
#따라서 양방향 그래프에서 루트 노드를 시작으로 하는 DFS탐색을 진행하며 이 과정속에서 부모-자식 관계를 정의할 수 있음. 

#변수 선언 및 입력 
n = int(input())
edges = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0] * (n+1)

# n-1개의 간선 정보를 입력받는다. 
for _ in range(n-1):
    x,y = tuple(map(int,input().split()))
    #간선 정보를 인접리스트에 넣는다. 
    edges[x].append(y)
    edges[y].append(x)

#트리 순회 + DFS 방식 + 진행되는 간선에 대해 부모,자식 관계 정의
def traversal(x):
    #노드 x에 연결된 간선을 살펴봄 
    for y in edges[x]:
        #아직 방문해본적 없는 노드라면 
        #트리의 부모-자식 관계가 결정됨
        #부모는 x, 자식이 y가 됨. 
        if not visited[y]:
            visited[y]=True
            parent[y] = x

            #추가적으로 탐색을 더 진행한다. 
            traversal(y)

# 1번부터 트리 순회를 진행
visited[1] = True
traversal(1)

#부모 노드를 출력한다. 
for i in range(2,n+1):
    print(parent[i])


#풀이1

# 테스트케이스가 visited 없어도 돌아가서 뺐지만 필요함
# 직전 코드에서 함수 안에서 visited 확인을 주석처리 해놔서 재제출

def find_end(point):  # point: 현재의 노드(서있는 위치)
    global result  # result: 결과를 저장할 변수인데 전역변수로 선언
    if result == 1 or visited[point] ==1:  # 종료조건: 결과를 찾았거나, 이미 방문했었던 노드이면 종료 / 0~99를 잇는 길을 찾았거나 visited 리스트에 point번 인덱스가 1인경우 더이상 찾지않기
        return
     
    visited[point] = 1  # 여기에서 방문체크 필요! (처음에 이걸 빠뜨렸음 > 위에 조건문이 if result==1 만 돌아가는 상황)
     
    if point == 99:  # 도착점 도착시 종료
        result = 1 
        return
     
    for node in routes[point]:  # routes[point]: 각 노드번호를 인덱스로 하는 값들은 그 노드에서 출발하는 노선들 > routes[1]이면 값은 [4, 3] > 이 두개의 값을 순회한다.
        find_end(node)  # find_end(4), find_end(3) 호출 > 종료되지 않는 경우: 
 
         
for _ in range(10):
    tc, N = map(int, input().split()) # tc: 테스트케이스 번호, N: 간선의 개수
    edges = list(map(int, input().split()))  # 간선 양 끝 노드들을 인풋받음(현재: 리스트 안에 구분없이 나열된 상태)
 
    routes = [[] for _ in range(100)]  
    # 각 출발점 노드를 인덱스로 하여 뻗어나갈 수 있는 도착점 노드를 적어놓음
    # ex) 0번 인덱스의 [1, 2]는 0 -> 1, 0 -> 2 로 갈수 있다는 말임
 
    for i in range(0, len(edges), 2):  # step 2씩 건너뛰기 > 짝수 인덱스만 짚는다 > 각 간선의 출발점
        # i : 몇 번째 간선인지
        # edges[i], edges[i+1] : 해당 간선의 시작점과 끝점 > 0, 2, 4... 짝수로 훑는 i번째는 시작, i+1은 자동으로 도착점
        # routes[edges[i]] : 시작점에서 갈 수 있는 경로 집합 > 리스트
        
        # routes[edges[i]] += [edges[i+1]]
        # routes[edges[i]] = routes[edges[i]] + [edges[i+1]] > 새로운 인덱스를 만드는 행위이므로 .append로 원본 수정 추천
        routes[edges[i]].append(edges[i+1])  # routes리스트 안의 리스트들은 해당 인덱스 번호의 노드에서 갈 수 있는 도착노드들 기입(최소 0개~최대 2개)
     
        # i=0) routes = [[1], [], [], [], ... []]
        # i=2) routes = [[1, 2], [], [], [], ... []] > 0번 노드(인덱스 번호)에서는 1번, 2번으로 향하는 두 갈래의 간선이 있다.
        # i=4) routes = [[1, 2], [4], [], [], ... []]
        # i=6) routes = [[1, 2], [4, 3], [], [], ... []] > 1번 노드에서는 4번, 3번 노드로 향하는 두 간선이 있다.
         
    result = 0   
    visited = [0]*100  # 정점의 개수가 최대 100개
 
    find_end(0)  # 함수 호출 > 출발점 0부터 시작
    print(f'#{tc} {result}')


#풀이02
def dfs(start, end):
    # 전역 변수 result를 global로 가져옴
    # > 테스트 for문 안이 아니라 밖에 있으면 0으로 초기화가 안됨
    global result
     
    # 현재 방문한 노드(start)를 방문 처리
    visited[start] = True
 
    # 현재 위치가 목표 지점(end)과 같다면 성공
    if start == end:
        # 결과값을 1로 변경
        result = 1
        # 현재 함수를 종료하고 이전 단계로 복귀
        return
 
    # 현재 노드와 연결된 다음 노드들을 하나씩 확인
    for next_node in graph[start]:
        # 만약 다음 노드를 아직 방문하지 않았다면 탐색
        if not visited[next_node]:
            # 다음 노드를 시작점으로 하여 다시 dfs를 호출
            dfs(next_node, end)
             
            # 재귀를 타고 들어갔다가 나왔을 때, 이미 목표를 찾았다면
            if result == 1:
                # 더 이상 다른 경로를 찾지 않고 즉시 함수를 종료
                return
 
for tc in range(1, 11):
    # 테스트 케이스 번호 _, 간선의 개수 M
    _, M = map(int, input().split())
 
    # 0번부터 99번까지의 노드를 담기 위해 100개의 빈 리스트를 만듦
    # > 인접 리스트 방식
    graph = [[] for _ in range(100)]
     
    # 한 줄로 들어오는 모든 간선 정보를 리스트로 받음
    link_lst = list(map(int, input().split()))
 
    # 리스트에서 두 개씩 짝을 지어 간선 정보를 그래프에 넣음
    # > 두 개씩 짝이므로 step = 2
    for i in range(0, M*2, 2):
        u, v = link_lst[i], link_lst[i+1]
        # 일방향 u에서 v로 가는 길만 저장
        graph[u].append(v)
 
    # 문제에서 정해준 시작점 S는 0, 도착점 G는 99
    S, G = 0, 99
     
    # 탐색 순서를 일정하게 맞추기 위해 각 노드의 인접 리스트를 정렬
    for i in range(100):
        graph[i].sort()
     
    # 각 테스트 케이스마다 방문 리스트와 결과값을 초기화
    visited = [False] * (100)
    result = 0
 
    # DFS 탐색
    dfs(S, G)
     
    print(f'#{tc} {result}')

def dfs(node):
    global answer
    visited[node] = 1
     
    if node == 99 or answer:
        answer = 1
        return
     
    if adj_list.get(node):
        for next_node in adj_list[node]:
            # 방문 체크 되어있으면 건너 뛰자
            if visited[next_node]:
                continue
 
            dfs(next_node)
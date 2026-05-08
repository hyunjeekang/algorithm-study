from collections import deque
N = int(input())

#구역 번호 -1 == 인덱스
populations = list(map(int, input().split()))

graph= []
for _ in range(N):
    info = list(map(int, input().split()))
    graph.append(info[1:])

answer = float('inf')

def is_connected(target_list):
    q = deque([(target_list[0])])
    
    visited = [False] * N
    while q:
        cur_idx = q.popleft()
        visited[cur_idx] = True
        
        for n_node in graph[cur_idx]:
            if not visited[n_node-1] and (n_node-1) in target_list:
                q.append(n_node-1)
    
    for node in target_list:
        if not visited[node]:
            return False
    return True

#모든 조합을 구해보자
for mask in range(1<<N):
    #A그룹: 1, B그룹: 0
    a_count = bin(mask).count('1')
    b_count = N - a_count
    
    a_list = []
    b_list = []
    for bit in range(N):
        if (mask & (1<<bit)) != 0 :
            a_list.append(bit)
        else:
            b_list.append(bit)
    
    #하나도 없으면 안됨
    if a_count == 0 or b_count == 0:
        continue
    
    #연결 안된게 있으면 안됨
    #연결? find?
    #그냥 bfs를 써볼까
    if not is_connected(a_list) or not is_connected(b_list):
        continue
    
    a_sum = 0
    b_sum = 0 
    
    for a_node in a_list:
        a_sum += populations[a_node]
    for b_node in b_list:
        b_sum += populations[b_node]
    diff = abs(a_sum - b_sum)
    answer = min(answer, diff)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
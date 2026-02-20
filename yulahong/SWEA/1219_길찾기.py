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
 
T = 10
 
for tc in range(1, T+1):
    # 못 갔다는 가정으로 0
    answer = 0
     
    _, M = map(int, input().split())
     
    # 이 숫자 입력의 길이는 M*2
    info = list(map(int, input().split()))
    adj_list = {}
    for i in range(0, M*2, 2):
        a, b = info[i], info[i+1]
        adj_list[a] = adj_list.get(a, [])
        adj_list[a].append(b)
     
    visited = [0]*100
    dfs(0)
     
    print(f'#{tc} {answer}')
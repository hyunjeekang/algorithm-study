from collections import deque

for test_case in range(1, 11):
    N, S = map(int, input().split())

    links = list(map(int, input().split()))

    adj = {}
    nodes = set()
    for i in range(0, N, 2):
        start, end = links[i], links[i+1]
        nodes.add(start)
        nodes.add(end)
        if start not in adj.keys():
            adj.setdefault(start, [end])
        else:
            if end not in adj[start]:
                adj[start].append(end)
    
    visited = {}
    for node in nodes:
        visited.setdefault(node, False)
    q = deque()
    q.append((S,0))

    max_dist = 0
    leaves = []

    while q:
        curr_node, cur_depth = q.popleft()
        
        if cur_depth > max_dist:
            max_dist = cur_depth
            leaves = [curr_node]
        elif cur_depth == max_dist:
            leaves.append(curr_node)
        
        if curr_node in adj:
            for neighbor in adj[curr_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, cur_depth+1))
    
    print(f'#{test_case}', max(leaves))
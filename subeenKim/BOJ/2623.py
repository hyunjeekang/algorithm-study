from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
come_after, come_before = defaultdict(set), defaultdict(set) # value가 key 이후에 나옴 / value가 key 이전에 나옴

for _ in range(M):
    singers = list(map(int, input().split()))
    n = singers[0]
    singers = singers[1:]
    for i, s in enumerate(singers):
        if i < n-1:
            for j in range(i+1, n):
                come_after[s].add(singers[j])
        
        if i > 0:
            for j in range(i):
                come_before[s].add(singers[j])
                
def get_order():
    
    visited = [False]*(N+1)
    visited[0] = True
    q = deque()
    for i in range(1, N+1):
        if not come_before[i]:
            order.append(i)
            visited[i] = True
            q.extend(list(come_after[i]))
    if not order:
        return visited
    
    while q:
        singer = q.popleft()
        if visited[singer]:
            continue
        for s in come_before[singer]:
            if not visited[s]:
                break
        else:
            order.append(singer)
            visited[singer] = True
            q.extend(list(come_after[singer]))
    
    return visited

order = []
visited = get_order()
if len(order) != N:
    print(0)
else:
    for o in order:
        print(o)
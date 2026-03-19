from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    return 0 <= r < N and 0 <= c < M

N, M, T = map(int, input().split())
deq_list = [deque(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    
    for i in range(x - 1, N, x):
        if d == 0:
            deq_list[i].rotate(k)  
        else:
            deq_list[i].rotate(-k) 

    visited = [[False] * M for _ in range(N)]
    is_deleted_this_turn = False 
    
    for r in range(N):
        for c in range(M):
            if deq_list[r][c] != 0 and not visited[r][c]:
                adj = [(r, c)] 
                q = deque([(r, c)])
                visited[r][c] = True
                num = deq_list[r][c]
                
                while q:
                    cur_r, cur_c = q.popleft()
                    
                    for i in range(4):
                        nr = cur_r + dr[i]
                        nc = (cur_c + dc[i]) % M 
                        
                        if is_range(nr, nc) and not visited[nr][nc]:
                            if deq_list[nr][nc] == num:
                                visited[nr][nc] = True
                                adj.append((nr, nc))
                                q.append((nr, nc))
                
                if len(adj) > 1:
                    is_deleted_this_turn = True
                    for a_r, a_c in adj:
                        deq_list[a_r][a_c] = 0

    if not is_deleted_this_turn:
        total_sum = 0
        count = 0
        for r in range(N):
            for c in range(M):
                if deq_list[r][c] != 0:
                    total_sum += deq_list[r][c]
                    count += 1
                    
        if count > 0:
            avg = total_sum / count
            for r in range(N):
                for c in range(M):
                    if deq_list[r][c] != 0:
                        if deq_list[r][c] > avg:
                            deq_list[r][c] -= 1
                        elif deq_list[r][c] < avg:
                            deq_list[r][c] += 1
total = 0
for deq in deq_list:
    total += sum(deq)
print(total)
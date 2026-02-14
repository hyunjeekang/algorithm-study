from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    q = deque()
    for i in range(1, N+1):
        q.append(i)
    
    pop_num = []
    while q:
        pop_num.append(q.popleft())
        if not q:
            break
        q.append(q.popleft())
    
    print(f'#{test_case}', pop_num[-1])
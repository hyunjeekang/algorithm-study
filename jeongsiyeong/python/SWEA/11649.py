from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    q= deque()
    for c in arr:
        q.append(c)
    
    for _ in range(M):
        q.append(q.popleft())
    
    print(f'#{test_case}', q.popleft())
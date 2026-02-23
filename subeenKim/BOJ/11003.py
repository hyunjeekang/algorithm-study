from collections import deque

N, L = map(int, input().split())
A = deque(list(map(int, input().split())))
IDX = deque([i for i in range(1, N+1)])
temp_list = deque([])
temp_idx = deque([])

for i in range(1, N+1):
    if temp_idx and temp_idx[0] < i-L+1:
        temp_list.popleft()
        temp_idx.popleft()

    a = A.popleft()
    if not temp_list:
        temp_list.append(a)
        temp_idx.append(IDX.popleft())
    else :
        while temp_list and temp_list[-1] > a:
            temp_list.pop()
            temp_idx.pop()
        temp_list.append(a)
        temp_idx.append(IDX.popleft())
    print(temp_list[0], end = ' ')
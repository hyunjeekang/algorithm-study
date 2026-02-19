from collections import deque

N, K = map(int, input().split())

#2진수 문자열을 10진수로: int('문자열', 2)
#정수를 2진수 문자열로: bin(정수)

numbers = []
code_map = {}
for i in range(N):
    number = int(input(), 2)
    numbers.append(number)

graph = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(i+1, N):
        if bin(numbers[i] ^ numbers[j]).count('1') == 1:
            graph[i+1].append(j+1)
            graph[j+1].append(i+1)

start_n, end_n = map(int, input().split())

parent = [0] * (N+1)
q = deque()
q.append(start_n)
parent[start_n] = -1

found = False
while q:
    cur_node = q.popleft()
    

    if cur_node == end_n:
        found = True
        break
    
    for next_node in graph[cur_node]:
        if parent[next_node] == 0:
            parent[next_node] = cur_node
            q.append(next_node)

if not found:
    print(-1)
else:
    path = []
    curr = end_n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    
    print(*path[::-1])
            


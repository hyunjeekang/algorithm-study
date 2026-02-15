# 2644 촌수계산
# 그래프 탐색 문제
#dfs로 해결
n = int(input())
a, b = map(int, input().split())
m = int(input())
parent = [-1 for _ in range(n+1)]
children = [ [] for _ in range(n+1)]

for _ in range(m):
    p, c = map(int, input().split())
    parent[c] = p
    children[p].append(c)

visit_stack = []
visit_stack.append((a, 0))
is_visited = [0 for _ in range(n+1)]

while(visit_stack):
    current_index, current_count = visit_stack.pop()
    is_visited[current_index] = 1
    if current_index == b:
        print(current_count)
        break
    if parent[current_index] != -1:
        if is_visited[parent[current_index]] == 0:
            visit_stack.append((parent[current_index], current_count+1))
    for child in children[current_index]:
        if not is_visited[child]:
            visit_stack.append((child, current_count+1))
else:
    print(-1)

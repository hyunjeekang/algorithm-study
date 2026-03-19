import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def check_connection(group, graph):
    q = deque([group[0]]) 
    visited = set([group[0]]) 
    
    while q:
        node = q.popleft()
        
        for neighbor in graph[node]:
            if neighbor in group and neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    if len(visited) == len(group):
        return True
    else:
        return False

def solve():
    N = int(input())
    
    populations = [0] + list(map(int, input().split()))
    
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        graph[i] = data[1:] 
        
    min_diff = float('inf') 
    nodes = [i for i in range(1, N + 1)]

    for i in range(1, N // 2 + 1):
        for group_a in combinations(nodes, i):
            group_a = list(group_a)

            group_b = [node for node in nodes if node not in group_a]
            
            if check_connection(group_a, graph) and check_connection(group_b, graph):
                
                pop_a = sum(populations[node] for node in group_a)
                pop_b = sum(populations[node] for node in group_b)
                
                diff = abs(pop_a - pop_b)
                min_diff = min(min_diff, diff) 
                
    if min_diff == float('inf'):
        print(-1)
    else:
        print(min_diff)

if __name__ == '__main__':
    solve()
# N개 중에 중복 없이 M개를 고른 수열

N, M = map(int, input().split())

def backtrack(temp_list):
    if len(temp_list) == M:
        order.append(temp_list[:])
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            temp_list.append(i)
            visited[i] = True
            backtrack(temp_list)
            temp_list.pop()
            visited[i] = False

order = []
visited = [False]*(N+1)
backtrack([])
for o in order:
    print(*o)
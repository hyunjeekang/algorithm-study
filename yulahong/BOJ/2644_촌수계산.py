# 부모 자식 간의 관계가 주어졌을 때 주어진 두 사람의 촌수를 계산하는 프로그램
# 첫째 줄: 사람의 수 > n
# 둘째 줄: 서로 다른 두 사람의 번호
# 셋째 줄: 부모 자식들 간의 관계의 개수 > m
# 넷째 줄: 부모 자식 간의 관계를 나타내는 두 번호 x,y가 각 줄에 나옴

from collections import deque
\
n = int(input())
person1, person2 = map(int, input().split()) # 둘째 줄: 서로 다른 두 사람의 번호
c = int(input()) # 셋째 줄: 부모 자식들 간의 관계의 개수 > m

#인접리스트 만들기
adj = [[] for _ in range(n+1)]
for _ in range (c):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0]*(n+1)

def bfs(node):
    q = deque([node]) #시작노드
    visited[node] = 1 #방문도장

    while q:
        cn = q.popleft()

        if cn == person2:
            return visited[cn] - 1

        for i in adj[cn]:
            if visited[i] == 0:
                visited[i] = visited[cn] + 1
                q.append(i)

    return -1

print(bfs(person1))



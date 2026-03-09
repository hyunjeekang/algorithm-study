# 상근 결혼식에 자신의 친구와 친구의 친구 초대
# 상근이의 동기 N명 이 학생들의 학번은 1-N 
# 상근의 학번 = 1
# 상근은 동기의 친구관계 리스트 소유
# 리스트 바탕으로 결혼식 초대할 사람
# 의 수 구하기

# 첫째 줄: 상근이의 동기 수 = n
# 둘째 줄: 상근의 친구리스트 = m
# 다음 줄부터 친구 관계

# 그래프 문제 > 인접리스트
# 상근이 있는 경우와 없는 경우 나누기
# bfs 쓰면 되나?

N = int(input())
m = int(input())

visted = [[] for _ in range(N+1)]

adj = [[] for _ in range(N+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for friend in adj[1]:
    visted[friend] = True

    for friends in adj[friend]:
        if friends != 1:
            visted[friends] = True

cnt = 0
for i in range(N+1):
    if visted[i]:
        cnt += 1
print(cnt)





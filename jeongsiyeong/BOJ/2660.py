import sys

# 입력 속도를 위해 사용
input = sys.stdin.readline

N = int(input())
INF = sys.maxsize # 충분히 큰 값

# 1. 그래프 초기화 (1번~N번 사람 사용을 위해 N+1 크기)
# 모든 거리를 무한대로 초기화
dist = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 거리는 0
for i in range(1, N + 1):
    dist[i][i] = 0

# 2. 친구 관계 입력 (거리 1)
while True:
    v1, v2 = map(int, input().split())
    if v1 == -1 and v2 == -1:
        break
    # 양방향 연결 (친구 관계는 쌍방향)
    dist[v1][v2] = 1
    dist[v2][v1] = 1

# 3. 플로이드-워셜 알고리즘 수행
# k: 거쳐가는 노드, i: 출발 노드, j: 도착 노드
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # i -> j 로 가는 길보다 i -> k -> j 로 가는 길이 더 짧으면 갱신
            # 단순히 min을 쓰는 것보다, 조건문을 달아주는 것이 불필요한 연산을 줄일 수 있음
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 4. 결과 계산
candidate_score = INF
scores = [] # 각 사람의 점수(가장 먼 친구와의 거리)를 저장할 리스트

for i in range(1, N + 1):
    # i번 사람의 점수 = i번 사람과 연결된 친구들 거리 중 가장 큰 값 (INF 제외)
    # dist[i][1:]은 0번 인덱스를 제외한 1~N번까지의 거리
    
    max_d = 0
    for j in range(1, N+1):
        if dist[i][j] != INF:
            max_d = max(max_d, dist[i][j])
            
    scores.append(max_d)
    
    # 전체 최소 점수(회장 점수) 갱신
    candidate_score = min(candidate_score, max_d)

# 5. 정답 출력
candidates = []
for i in range(N):
    # i번째 사람의 점수가 최소 점수와 같다면 후보 등록
    # scores 리스트는 0번 인덱스가 1번 사람이므로 index + 1 해줘야 함
    if scores[i] == candidate_score:
        candidates.append(i + 1)
candidates.sort()

print(candidate_score, len(candidates))
print(*candidates)
import sys
from collections import deque

input = sys.stdin.readline
grid = [input().strip() for _ in range(5)]

# 중복 방문 방지를 위한 집합 (set)
visited_combs = set()

q = deque()
ans = 0

# 1. 초기화: 모든 25개 칸을 각각 시작점으로 큐에 넣음
# 큐 저장 형태: (현재 포함된 좌표들의 리스트, S의 수, Y의 수)
for r in range(5):
    for c in range(5):
        # 방문 처리를 위해 튜플로 변환 (좌표 하나라도 튜플로 감싸야 함)
        start_node = ((r, c),) 
        visited_combs.add(start_node)
        
        is_S = 1 if grid[r][c] == 'S' else 0
        is_Y = 1 if grid[r][c] == 'Y' else 0
        
        # (좌표리스트, S개수, Y개수)
        q.append((list(start_node), is_S, is_Y))

# 상하좌우
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while q:
    curr_nodes, s_cnt, y_cnt = q.popleft()

    # 7명이 모였을 때
    if len(curr_nodes) == 7:
        if s_cnt >= 4:
            ans += 1
        continue
    
    # 이번 단계에서 갈 수 있는 후보지들을 찾음 (adj_candidates)
    adj_candidates = set()
    for r, c in curr_nodes:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                # 이미 그룹에 포함된 애가 아니라면 후보에 추가
                if (nr, nc) not in curr_nodes:
                    adj_candidates.add((nr, nc))
    
    # 후보지들을 하나씩 붙여서 새 그룹 만들기
    for nr, nc in adj_candidates:
        next_nodes = curr_nodes + [(nr, nc)]
        
        # 중복 체크를 위해 정렬 후 튜플 변환 (순서 무관하게 만들기)
        # 예: [(0,0), (0,1)] 과 [(0,1), (0,0)]을 같은 것으로 취급
        next_nodes.sort() 
        next_key = tuple(next_nodes)
        
        if next_key not in visited_combs:
            visited_combs.add(next_key)
            
            # S, Y 개수 갱신
            next_s = s_cnt + (1 if grid[nr][nc] == 'S' else 0)
            next_y = y_cnt + (1 if grid[nr][nc] == 'Y' else 0)
            
            # 가지치기: 임도연 파(Y)가 4명이 되면 더 이상 가망 없음 (7명 중 4명이 Y면 S는 최대 3명)
            if next_y >= 4:
                continue
                
            q.append((list(next_nodes), next_s, next_y))

print(ans)
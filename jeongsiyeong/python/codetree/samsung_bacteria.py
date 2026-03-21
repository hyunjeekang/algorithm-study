from collections import deque
import heapq
from copy import deepcopy

# 첫 줄에 정수 N, Q가 공백으로 구분되어 주어진다
N, Q = map(int, input().split())

# N*N 크기의 정사각형 형태의 배양 용기
arr = [[-1] * N for _ in range(N)]

# 상하좌우
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_range(r, c):
    return 0 <= r < N and 0 <= c < N

for q_idx in range(Q):
    # 1. 새로운 미생물 덮어쓰기
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = q_idx

    # 2. 미생물 덩어리(연결 컴포넌트) 개수 세기 및 상대 좌표 추출
    visited = [[False] * N for _ in range(N)]
    mic_coords = [set() for _ in range(Q)]
    component_count = [0] * Q  # 미생물별 덩어리 개수
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] != -1 and not visited[r][c]:
                micro_num = arr[r][c]
                component_count[micro_num] += 1
                
                # BFS로 한 덩어리 탐색
                q = deque([(r, c)])
                visited[r][c] = True
                cells = [(r, c)]
                
                while q:
                    cur_r, cur_c = q.popleft()
                    for i in range(4):
                        nr, nc = cur_r + dr[i], cur_c + dc[i]
                        if is_range(nr, nc) and arr[nr][nc] == micro_num and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            cells.append((nr, nc))
                
                # 첫 번째 덩어리일 때만 상대 좌표(형태) 저장 (min_r, min_c 기준)
                if component_count[micro_num] == 1:
                    min_r = min(cell[0] for cell in cells)
                    min_c = min(cell[1] for cell in cells)
                    for cr, cc in cells:
                        mic_coords[micro_num].add((cr - min_r, cc - min_c))
                        
    # 🚨 핵심 룰: 두 조각 이상으로 찢어진 미생물은 완전 소멸!
    for k in range(Q):
        if component_count[k] >= 2:
            mic_coords[k].clear()  # 확실하게 자기 번호(k)를 지웁니다!
            for r in range(N):
                for c in range(N):
                    if arr[r][c] == k:
                        arr[r][c] = -1

    # 3. 새로운 배양 용기로 이동
    new_arr = [[-1] * N for _ in range(N)]
    pq = []
    
    for k in range(Q):
        if len(mic_coords[k]) > 0:
            heapq.heappush(pq, (-len(mic_coords[k]), k))

    while pq:
        cur_microbe = heapq.heappop(pq)[1]
        is_copyable = False        
        
        # 만약 정답이 다르게 나온다면 for c: for r: 로 순서를 뒤집어주세요! (x, y 기준)
        for r in range(N):
            for c in range(N):
                # 🚨 주의: 시작 기준점인 new_arr[r][c] 가 -1일 필요는 없습니다!
                can_place = True
                for rel_r, rel_c in mic_coords[cur_microbe]:
                    nr = r + rel_r
                    nc = c + rel_c
                    if not is_range(nr, nc) or new_arr[nr][nc] != -1:
                        can_place = False
                        break
                
                if can_place:
                    for rel_r, rel_c in mic_coords[cur_microbe]:
                        nr = r + rel_r
                        nc = c + rel_c
                        new_arr[nr][nc] = cur_microbe
                    is_copyable = True
                    break
            if is_copyable:
                break
                
        if not is_copyable:
            mic_coords[cur_microbe].clear()

    arr = deepcopy(new_arr)   

    # 4. 실험 결과 기록 (출력)
    experiment_score = 0
    adj_pairs = set()
    
    for r in range(N):
        for c in range(N):
            u = arr[r][c]
            if u == -1: continue
            
            for dr_idx, dc_idx in [(0, 1), (1, 0)]:
                nr, nc = r + dr_idx, c + dc_idx
                if is_range(nr, nc):
                    v = arr[nr][nc]
                    if v != -1 and u != v:
                        adj_pairs.add(tuple(sorted((u, v))))

    for u, v in adj_pairs:
        area_u = len(mic_coords[u])
        area_v = len(mic_coords[v])
        experiment_score += area_u * area_v
    
    print(experiment_score)
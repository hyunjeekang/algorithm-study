from collections import deque
import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용 권장
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

start_r, start_c, start_dir = map(int, input().split())
end_r, end_c, end_dir = map(int, input().split())

# 문제의 방향 정의: 1:동, 2:서, 3:남, 4:북
# 코드 내 사용 인덱스(0~3): 0:동, 1:서, 2:남, 3:북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# (행, 열, 방향) 3차원 방문 배열
visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]

def bfs():
    q = deque()
    # 입력받은 좌표는 1-based이므로 0-based로 변환
    sr, sc, sd = start_r - 1, start_c - 1, start_dir - 1
    er, ec, ed = end_r - 1, end_c - 1, end_dir - 1
    
    q.append((sr, sc, sd, 0))
    visited[sr][sc][sd] = True

    while q:
        r, c, d, cnt = q.popleft()

        # 목적지 도착 및 방향까지 일치하면 종료
        if r == er and c == ec and d == ed:
            return cnt

        # 1. 명령 Go k: 현재 방향으로 1, 2, 3칸 이동
        for k in range(1, 4):
            nr = r + dr[d] * k
            nc = c + dc[d] * k

            # 맵을 벗어나거나 벽을 만나면 더 이상 이동 불가 (break 중요!)
            if not (0 <= nr < M and 0 <= nc < N) or arr[nr][nc] == 1:
                break
            
            # 방문하지 않은 곳이면 큐에 추가
            if not visited[nr][nc][d]:
                visited[nr][nc][d] = True
                q.append((nr, nc, d, cnt + 1))

        # 2. 명령 Turn: 왼쪽 또는 오른쪽 90도 회전
        # 동(0), 서(1), 남(2), 북(3)
        # 동(0) -> 좌:북(3), 우:남(2)
        # 서(1) -> 좌:남(2), 우:북(3)
        # 남(2) -> 좌:동(0), 우:서(1)
        # 북(3) -> 좌:서(1), 우:동(0)
        
        # 각 방향에서의 왼쪽, 오른쪽 회전 결과 매핑
        # [왼쪽 회전 결과, 오른쪽 회전 결과]
        turn_map = {
            0: [3, 2], # 동
            1: [2, 3], # 서
            2: [0, 1], # 남
            3: [1, 0]  # 북
        }
        
        for nd in turn_map[d]:
            if not visited[r][c][nd]:
                visited[r][c][nd] = True
                q.append((r, c, nd, cnt + 1))

print(bfs())
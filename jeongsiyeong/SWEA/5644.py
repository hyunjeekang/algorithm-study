# 방향 정보 (0:X, 1:상, 2:우, 3:하, 4:좌)
# 문제 좌표계: (1,1)이 좌상단 -> y가 행, x가 열
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

def solve():
    T = int(input())
    for test_case in range(1, T + 1):
        M, A = map(int, input().split())
        
        # 이동 정보 (M개의 이동)
        move_a = list(map(int, input().split()))
        move_b = list(map(int, input().split()))
        
        # 충전소 정보 저장 (x, y, c, p) -> 리스트로 관리
        # 인덱스 0부터 A-1까지가 각 충전소의 ID가 됨
        bcs = [list(map(int, input().split())) for _ in range(A)]
        
        # 사용자 A, B의 초기 위치 (문제 좌표 그대로 사용: 1~10)
        ax, ay = 1, 1
        bx, by = 10, 10
        
        # 충전량 합계 계산 함수 (현재 위치에서 최대 충전량 반환)
        def get_max_charge(ax, ay, bx, by):
            # 1. A가 접속 가능한 충전소 리스트
            cand_a = []
            for i in range(A):
                # 거리 계산: |x1-x2| + |y1-y2| <= C
                dist = abs(ax - bcs[i][0]) + abs(ay - bcs[i][1])
                if dist <= bcs[i][2]:
                    cand_a.append(i)
            
            # 2. B가 접속 가능한 충전소 리스트
            cand_b = []
            for i in range(A):
                dist = abs(bx - bcs[i][0]) + abs(by - bcs[i][1])
                if dist <= bcs[i][2]:
                    cand_b.append(i)
            
            # 3. 모든 조합(Combination)을 비교하여 최댓값 찾기
            # 경우의 수 계산을 위해 '선택 안 함'을 의미하는 더미 값(-1) 추가
            if not cand_a: cand_a.append(-1)
            if not cand_b: cand_b.append(-1)
            
            max_val = 0
            
            for a_idx in cand_a:
                for b_idx in cand_b:
                    temp_val = 0
                    
                    # A의 충전량
                    if a_idx != -1:
                        temp_val += bcs[a_idx][3]
                    
                    # B의 충전량
                    if b_idx != -1:
                        temp_val += bcs[b_idx][3]
                    
                    # 같은 충전소를 공유하는 경우
                    if a_idx != -1 and b_idx != -1 and a_idx == b_idx:
                        temp_val //= 2 # 반으로 나누기
                        temp_val = bcs[a_idx][3] # 공유하면 그냥 P 하나값
                        
                    max_val = max(max_val, temp_val)
                    
            return max_val

        # 0초(초기 위치) 충전
        total_charge = get_max_charge(ax, ay, bx, by)
        
        # 1초 ~ M초 이동하며 충전
        for t in range(M):
            # A 이동
            ax += dx[move_a[t]]
            ay += dy[move_a[t]]
            # B 이동
            bx += dx[move_b[t]]
            by += dy[move_b[t]]
            
            # 이동 후 충전
            total_charge += get_max_charge(ax, ay, bx, by)
            
        print(f"#{test_case} {total_charge}")

solve()
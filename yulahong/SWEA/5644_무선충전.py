# [코드 설계도 및 회고록]
 
# # 1. 핵심 설계 포인트 (Key Realizations)
 
# (1) 좌표계의 일치:
#     - 문제는 (X, Y)로 주어지지만 리스트 인덱스는 (R, C)임.
#     - 델타 배열(dr, dc)을 정의할 때 문제의 방향(1:상, 2:우...)과 인덱스 변화량을 정확히 매칭하는 것이 시작임.
 
# (2) 시간의 흐름 (T=0의 중요성):
#     - 사용자는 0초(초기 위치)부터 이미 충전 범위에 있을 수 있음.
#     - 총 이동 횟수가 M이라면, 충전 기회는 0초부터 M초까지 총 'M+1'번임.
 
# (3) 겹치는 BC 처리 (조합의 원리):
#     - 한 사용자가 여러 BC 범위에 동시에 들어갈 수 있음.
#     - 두 사용자가 같은 BC를 공유하면 충전량을 반씩 나누지만,
#         > 결국 "두 사람 충전량의 합"을 구하는 것이므로 그냥 해당 BC의 파워 P와 같음.
#     - 가장 안전한 방법은 A의 선택지(i)와 B의 선택지(j)를 모든 조합으로 맞춰보는 '전수 조사'임.
 
# --------------------------------------------------
 
# # 2. 상세 로직 흐름 (Step-by-Step)
 
# 1. [입력]
#     - 사용자의 이동 정보와 BC의 정보를 저장함.
#     - BC 정보는 (R, C, 범위, 파워) 튜플/리스트 형태로 관리.
 
# 2. [M+1번의 반복문]
#     - 매 초마다 다음 과정을 수행:
 
#     a. [접속 가능 BC 리스트업]
#         - 사용자 A, B의 현재 위치에서 모든 BC와의 거리를 계산함.
#         - 거리 공식: D = |r1 - r2| + |c1 - c2| (맨해튼 거리)
#         - D <= 범위(C) 인 모든 BC의 '인덱스'를 각자의 후보 리스트에 담음.
 
#     b. [최적 조합 탐색]
#         - A의 후보와 B의 후보를 이중 for문으로 순회함.
#         - 만약 같은 BC(i == j)를 골랐다면? 합계 = P_i (나눠 가져도 합은 그대로)
#         - 만약 서로 다른 BC(i != j)를 골랐다면? 합계 = P_i + P_j
#         - 이 중 가장 큰 합계(Max)를 찾아 전체 결과에 누적함.
 
#     c. [위치 이동]
#         - M초가 되기 전까지는 입력받은 방향대로 A, B의 좌표를 업데이트함.
 

T = int(input())

# 이동 방향 정의 (0:제자리, 1:상, 2:우, 3:하, 4:좌)
# 문제의 (x, y) 좌표계와 리스트의 (r, c) 인덱스가 다르므로 이를 고려하여 설정함
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]
 
for tc in range(1, T+1):
    # 이번 테스트 케이스의 총 충전 합산량을 저장할 변수
    answer = 0
 
    # M: 이동 횟수(초), N: 배터리 충전기(BC)의 개수
    M, N = map(int, input().split())
 
    # 사용자 A와 B의 매 초 이동 방향 정보를 리스트로 받음
    pos_A = list(map(int, input().split()))
    pos_B = list(map(int, input().split()))
 
    # BC의 정보를 저장할 리스트
    BC_info = [0]*N
    for i in range(N):
        # [x, y, 범위, 충전량] 순서로 저장됨
        BC_info[i] = list(map(int, input().split()))
 
    # 사용자의 현재 위치를 저장
    # 위치가 바뀌기 때문에 튜플이 아닌 리스트로 설정
    # A는 (1,1), B는 (10,10)에서 시작
    # 시작 위치가 각각 정해져있기 때문에 초기값 설정
    # [행, 열] 형태의 리스트로 만들어 위치 변화를 실시간으로 반영
    human_rcs = [[1, 1], [10, 10]]
 
    # 0초(초기 위치)부터 M초까지 총 M+1번 충전을 시도
    # 충전 > M+1 > 초기 위치에서부터 충전이 가능해서 M+1
    for time in range(M+1):
        # 충전을 하고 이동
        # 충전 가능한 위치를 탐색 > 최적 충전량을 충전 > 이동
 
        # [1단계: 충전 가능한 BC 찾기]
 
        # charge_idxs[0]은 사용자 A가, [1]은 B가 접속 가능한 BC의 인덱스 번호를 담음
        charge_idxs = [[], []]
 
        # 두 명의 사용자에 대해 반복
        # A, B 중 누구를 돌지 > 0 / 1
        # i : A인지 B인지 > 사람 번호
        for i in range(2):
            # 현재 사용자의 위치
            r, c = human_rcs[i]
 
            # 모든 BC를 검사
            # 어떤 충전소인지 선택
            # j : 충전소 번호
            for j in range(N):
                BC_r, BC_c, coverage, charge_amount = BC_info[j]
 
                # 맨해튼 거리 계산: |X1 - X2| + |Y1 - Y2|
                # 거리가 BC의 충전 범위(coverage) 이내라면 목록에 추가
                if abs(r-BC_r) + abs(c-BC_c) <= coverage:
                    charge_idxs[i].append(j)
 
        # [2단계: 최적의 충전 조합 결정 (조합 전수 조사)]
 
        # 이번 초에 A와 B가 얻을 수 있는 최대 충전 합계
        charge = 0
 
        # a. 사용자 A는 접속 가능한 BC가 없고 B만 있는 경우
        if not charge_idxs[0]:
 
            # 사용자 B의 접속가능한 BC를 순회
            for i in charge_idxs[1]:
                # 지금 내가 보고 있는 BC의 파워가 다른 파워들보다 더 큰지 판별
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]
 
        # b. 사용자 B는 접속 가능한 BC가 없고 A만 있는 경우
        elif not charge_idxs[1]:
 
            # 사용자 A의 접속가능한 BC를 순회
            for i in charge_idxs[0]:
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]
 
        # c. A와 B 둘 다 접속 가능한 BC가 하나 이상 있는 경우
        else:
 
            # A가 선택 가능한 모든 BC(i)와 B가 선택 가능한 모든 BC(j)를 대조
            # i : A의 충전소 번호
            for i in charge_idxs[0]:
                # j : B의 충전소 번호
                for j in charge_idxs[1]:
 
                    # [중복 상황] 같은 BC를 선택한 경우
                    if i == j:
                        # 둘이 나눠 가져도 결국 합산은 BC 한 개의 충전량과 같음
                        if BC_info[i][3] > charge:
                            charge = BC_info[i][3]
                    # [개별 상황] 서로 다른 BC를 선택한 경우
                    else:
                        # 각자의 충전량을 온전히 더함
                        if BC_info[i][3] + BC_info[j][3] > charge:
                            charge = BC_info[i][3] + BC_info[j][3]
 
        # 이번 초에 얻은 최적의 충전량을 총합에 더함
        answer += charge
 
        # [3단계: 사용자 이동]
 
        # M초일 때는 마지막 충전 후 루프를 종료 (이동하지 않음)
        if time == M:
            break
 
        # A와 B의 위치를 다음 방향으로 이동
        human_rcs[0][0] += dr[pos_A[time]]
        human_rcs[0][1] += dc[pos_A[time]]
 
        human_rcs[1][0] += dr[pos_B[time]]
        human_rcs[1][1] += dc[pos_B[time]]
 
    print(f'#{tc} {answer}')
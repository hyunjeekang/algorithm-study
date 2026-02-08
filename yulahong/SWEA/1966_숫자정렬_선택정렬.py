T = int(input())

for tc in range(1, T+1):

    N = int(input())
    N_num = list(map(int, input().split()))
    # i : 지금 자리를 정하고 싶어하는 인덱스
    # min_idx : 현재 회차에서 최소값으로 지정될 인덱스
    # j : 현재 회차에서 순회중인 인덱스
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if N_num[min_idx] > N_num[j]:
                min_idx = j
        N_num[i], N_num[min_idx] = N_num[min_idx], N_num[i]
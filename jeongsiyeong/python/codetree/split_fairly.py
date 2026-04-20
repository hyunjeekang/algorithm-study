N, K = map(int, input().split())

synergys = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')

for mask in range(1 << N):
    a_count = bin(mask).count('1')
    b_count = N - a_count

    if a_count < K or b_count < K:
        continue

    a_idx = []
    b_idx = []

    for bit in range(N):
        if (mask & (1<<bit)) != 0:
            a_idx.append(bit)
        else:
            b_idx.append(bit)
    a_pow = 0
    b_pow = 0
    for i in range(len(a_idx)):
        for j in range(i+1, len(a_idx)):
            a_pow += synergys[a_idx[i]][a_idx[j]] + synergys[a_idx[j]][a_idx[i]]
    for i in range(len(b_idx)):
        for j in range(i+1, len(b_idx)):
            b_pow += synergys[b_idx[i]][b_idx[j]] + synergys[b_idx[j]][b_idx[i]]
    cur_synergys = abs(a_pow - b_pow)
    answer = min(answer, cur_synergys)
print(answer)

    

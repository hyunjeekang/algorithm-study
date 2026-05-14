T = int(input())

def find_case(idx):
    global N, answer, answer_cages
    if idx == N+1:
        for l,r,s in commands:
            if sum(cages[l:r+1]) != s :
                return
        cur_sum = sum(cages)
        if answer < cur_sum:
            answer = cur_sum
            answer_cages = " ".join(map(str,cages[1:]))
        return
    
    for i in range(X+1):
        cages[idx] = i
        find_case(idx+1)

for test_case in range(1, T+1):
    N, X, M = map(int,input().split())

    cages = [0] * (N+1)
    commands = []
    answer = -1
    answer_cages = "-1"
    
    for _ in range(M):
        l, r, s = map(int, input().split())
        commands.append((l,r,s))

    find_case(1)

    print(f'#{test_case} {answer_cages}')
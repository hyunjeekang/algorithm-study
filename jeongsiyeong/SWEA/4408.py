T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    passway = [0]*201

    for _ in range(N):
        start, end = map(int,input().split())

        if start > end:
            start, end = end, start
         
        s_idx = (start+1) // 2
        e_idx = (end+1) // 2
 
        for i in range(s_idx, e_idx+1):
            passway[i] += 1
     
    print(f'#{test_case}', max(passway))
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    comb = deque()

    for i in range(N):
        comb.append((i,arr[i]))

        cnt = 0
        while comb:
            max_val = max(comb,key=lambda x: x[1])[1]
            cur_i,cur_score = comb.popleft()

            # 종료조건 
            if cur_i == M and cur_score == max_val:
                cnt += 1
                print(cnt)
                break 

            if cur_i != M and cur_score < max_val:
                comb.append((cur_i,cur_score))

            elif cur_i == M and cur_score < max_val:
                comb.append((cur_i, cur_score))

            elif cur_i != M and cur_score == max_val:
                cnt += 1
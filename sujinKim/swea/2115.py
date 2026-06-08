# 벌꿀채취 ~
import sys 
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split()) 
    # N : 배열의 크기 / M : 벌통 수 / C : 벌꿀최대양 
    arr = [list(map(int,input().split())) for _ in range(N)]

    #로직을 어떻게 해야할까 ~?
    #결과값 : 두 일꾼이 꿀을 채취하여 얻을 수 있는 최대 수익 

    # 배열을 돌아다니면서 연속된 M개를 뽑고, 그 뽑은 값의 합이 C이하여야하고, 
    # 뽑았을때, 각각 제곱의 합이 더 큰 값이어야함 

    # 1. 배열에서 차례대로 M개를 뽑았을 떄

    # 2. 그 M개에서 몇개를 뽑든 C 이하의 수로 뽑을 떄 

    # 3. M개에서 뽑은수의 제곱을 더해서 어떤 리스트의 값에 저장해놓고,
    # 4. M개에서 다른 조합으로 뽑았을 떄, 그 수가 더 크다면 갱신 
    # 이런식으로 최댓값끼리 더한 값이 정답?  

    # 근데 만약에 M=2 C=17인데, 10 1 9 8 이런식이야. 그러면 101 81+64 이나까 98이 더 유리 
    # 그래서 무조건 큰수는 ㄴㄴ 인듯 
    # 위치 + 조합 
############ 여기까지 나 혼자 생각한 로직 ############
    profit = [[0]*N for _ in range(N)]  # 이익의 배열을 적는 곳 

    # 1. 각 위치별 최대 수익 계산 
    for i in range(N):
        for j in range(N-M+1):
            ggul = arr[i][j:j+M] # 꿀... 배열의  i,j~j+M까지의 값
            max_profit = 0 # 초기설정 

            # 부분집합? 조합? 생각
            for bit in range(1<<M): # 비트?...
                total = 0
                money = 0

                for k in range(M):
                    if bit & (1<<k):
                        total += ggul[k]
                        money += ggul[k]**2

                if total <= C:
                    max_profit = max(max_profit,money)

            profit[i][j] = max_profit

    # 2. 두 일꾼 위치 고르기 
    answer = 0

    for i1 in range(N):
        for j1 in range(N-M+1):
            for i2 in range(N):
                for j2 in range(N-M+1):

                    # 같은 위치 또는 겹치는 경우 제외 
                    if i1 == i2 and not (j1+M <= j2 or j2 +M <= j1):
                        continue 

                    answer = max(answer,profit[i1][j1] + profit[i2][j2])

    print(f'#{tc} {answer}')



                

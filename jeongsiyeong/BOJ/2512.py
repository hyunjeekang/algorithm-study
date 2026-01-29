#백준 2512번 예산 문제
#정석은 이진 탐색(Binary Search)지만 그리디로 해결

#지방의 수
total_regions = int(input())

#각 지방이 요청한 예산
budgets = list(map(int, input().split()))

#총 예산
total_budget = int(input())

budgets.sort()


for i in range(total_regions):
    # 현재 시점에서 남은 지방들에게 공평하게 나눠주자
    limit = total_budget // (total_regions - i)

    #현재 지방이 공평한 배분액보다 작거나 같다면?
    if budgets[i] <= limit:
        #요청한 만큼 줘버리자
        total_budget -= budgets[i]
    else:
        #요청한 금액이 배분액보다 크다면?
        #현재 배분액으로 결정!
        print(limit)
        exit()
#모든 지방에 돈을 다 줬는데도 예산이 남네?
#가장 큰 요청 금액이 상한선
print(budgets[-1])
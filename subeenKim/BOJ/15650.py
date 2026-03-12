# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

N, M = map(int, input().split())

def backtrack(start):
    if len(temp_list) == M:
        print(*temp_list)
        return
    
    for i in range(start, N+1):
        temp_list.append(i)
        backtrack(i+1) # 지금 선택한 수보다 1 큰 수부터 또 탐색 (중복 방지)
        temp_list.pop()

temp_list = []
backtrack(1)
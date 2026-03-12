# B = 선반의 높이
# N = 점원 수
# H = 점원의 키 

# 변수
T = int(input())

for tc in range(1, T+1):
    path = [] #조합 담아놓을 리스트
    N, B = map(int, input().split()) #점원 수
    S = list(map(int, input().split())) 
    sum_lst = []    

    def recur(cnt, prev):
        if sum(path) >= B:
            sum_lst.append(sum(path))
    
        for i in range(prev,N):
            path.append(S[i])
            recur(cnt+1, i+1)
            path.pop()
    
    recur(0,0)
    ans = min(sum_lst) - B

    print(f'#{tc} {ans}')


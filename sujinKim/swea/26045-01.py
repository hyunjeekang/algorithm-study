#부분수열 응용버전 
# 문제 
# 정수 리스트 A와 B가 주어진다. 
# A에서 몇 개의 원소를 삭제해서, 남은 수열이 B를 부분수열로 포함하도록 만들고 싶다. 
# 삭제는 A에서만, 순서유지, 목표는 B를 부분수열로 만들기 위해 삭제해야하는 최소 개수
# 어떤 방법으로도 B를 부분수열로 만들 수 없다면 -1을 출력

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #map의 역할이 뭐였더라? 문자열로 들어온 토큰들을 int로 변환해주는 변환기 
    #최소삭제개수 : N-M
    i = j = 0   #i,j 값 잊지 않고 초기화하기 
    # count = 0
    for i in range(N):
        if j < M and A[i] == B[j]: #아직 B를 다 못 맞췄고, 값이 같다면 
            j += 1
        # if A[i] != B[j]:  #만약 각각의 인덱스에 해당하는 값이 다르다면 
        #     count +=1   #거기에 해당하는 A의 인덱스값을 제거한다. 
    if j == M:  # A와 B에 해당하는 값이 같다면 
        # j += 1        # j의 값을 1씩 증가한다 = 즉, B를 증가하기 위해 옆으로 옮기는거지 
        print(f'#{tc} {N-M}')
           
    else:
        print(f'#{tc}-1')
        

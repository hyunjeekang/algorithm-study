#부분 수열 

T = int(input())   #테스트케이스의 개수를 입력받는다. 

for tc in range(1,T+1):  #테스트케이스 개수만큼 돌때 
    # N = int(input()) 
    # M = int(input())
    N,M = map(int, input().split()) #A리스트와 B리스트의 개수를 각각 입력받는다. 

    A = list(map(int,input().split())) #A리스트의 배열을 입력받는다. 
    B = list(map(int,input().split())) #B리스트의 배열을 입력받는다. 


#range() vs range(len()) 
#range()는 숫자범위 시퀀스: 그래서 리스트를 못넣음 근데 나는 계속 넣고 앉았음 
#range(len()) 리스트 등 자료형의 인덱스를 생성해 요소에 접근하는 데 사용
#range(stop):0부터 stop 미만까지의 숫자를 생성 
#range(len(seq)):리스트나 문자열의 길이만큼 인덱스 생성 
    i = j = 0
    for i in range(len(A)):  #입력받은 A리스트의 길이만큼 돌때
    # for i in range(N): #len(A)이나 N이나 같을듯 ? 
        if A[i] == B[j]: #A의 i번쨰와 B의 j번째의 수가 같을떄 -> 그러면 초기값이 필요하겠지? 
            j += 1 #수가 같을떄마다 B의 j번째수를 늘림. 
        if j == M: #만약에 j가 총 개수와 같다면 
            break #멈춤 즉, 빠져나옴 
        #근데 만약에 여기서 break이 없다면 어떻게 되는걸까? 

#if if : 모든 조건식을 다 검사한다. 
#if elif : if부터 조건이 맞으면 그 뒤에 오는 elif 조건식은 검사하지 않고 건너뛴다. 


    if j == M: #j가 M개랑 같게 된다면 예스 
        print(f'#{tc} YES')
    elif j != M:
        print(f'#{tc} NO') #아니면 노 
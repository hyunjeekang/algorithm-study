N,M = map(int,input().split())
##중복순열
arr = [i for i in range(1,N+1)] # N에 해당하는 숫자들을 arr에 넣기 
# visited = [False]*N # 중복순열이라 방문배열이 필요 없을줄 알았는데 필요하나?
result = [0]*M # 필요한수만큼 만들기 

def recur(index):
    if index == M: # 만약에 인덱스의 값과 엠값이 같으면 
        print(*result) # 출력 
        return
    for r in range(N): # arr 배열에서 하나씩 꺼낼건데,, 
        result[index] = arr[r] # 결과값의 인덱스에 arr의 값을 넣는 s
        recur(index+1)  # 그 다음 인덱스의 값을 함수에 호출한다. 

recur(0) 

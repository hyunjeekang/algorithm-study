# ㅈ전체 우리의 길이 N 
# X = 한 우리에 들어갈 수 있는 햄스터의 수 
# M = 조건이 나오는 line 의 수 


# 조건에 포함되지 않는 칸이 있으면 -> 무조건 최대 햄스터 때려버리기 

# 조건을 첫번째 arr 만 시도하고 넘어가버림 -> flagging? 기법을 활용해얌 


# 조건에 맞는지 확인하는 함수  
def check(i,r,cnt,res):
    c = 0
    for idx in range(i-1,r): 
        c += res[idx]
    if c == cnt:
        return True
    return False

# 중복 순열의 목적: 모든 경우의 수를 탐색하면서 선택(append) 와 취소(pop)
def cnt_hamster(depth): #중복순열
    if depth == N: 
        is_ok = True
        for condition in arr:
            i, r, cnt = condition
            if not check(i,r,cnt,res): # 조건에 부합하는지 확인
                is_ok = False # 적합하지 않은 조건이 있다. 
                break
        if is_ok: # flag 가 다 체크되고 나면
            results.append(list(res))
        return
    
    for num in range(X+1):
        res.append(num)
        cnt_hamster(depth+1)
        res.pop()

T =int(input())
for tc in range(1,T+1):
    N, X, M = map(int,input().split())
    arr = []
    results = []
    # res_count = -1 # 각 res total count 
    res = [] # 결과 res 
    # ans 로 저장 
    for _ in range(M):
        i, r, cnt = map(int,input().split())
        arr.append((i,r,cnt))

    cnt_hamster(0)
    # results.sort() # 사전 순으롤 정렬
    ans = []
    if len(results) >= 1: # 1개라도 조건에 부합하는 결과가 있으면 
        max_sum = max([sum(res) for res in results]) # int 값으로 주어짐
        for res in results:
            if sum(res) == max_sum: 
                ans.append(list(res))
        ans.sort()
        print(f'#{tc}',*ans[0])
    else:
        print(f'#{tc}',-1)

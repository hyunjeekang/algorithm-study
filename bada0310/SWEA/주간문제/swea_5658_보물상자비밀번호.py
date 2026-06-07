# 원형큐? 문제 
# -> 애매한 이유 4면이 있음으로 규칙성이 존재할 수 있음 
# 예시가 왜 3번만에 통과가 되는지 모르겠으니? 모든 경우를 다보겠다. 

# head 포인터와 tail 포인터를 옮기는 식으로 
# 3 개씩 끊어서  str 객체로 만들기 -> 전체 ans arr 에 저장 

T = int(input())

for tc in range(1,T+1):
    N, K =map(int,input().split())
    arr = input()
    
    L = N // 4
    candid_set = set()
    
    for head in range(N):
        rear = head+L
        if rear <= N:
            item = arr[head:rear]
        
        else: # 앞부분 문자를 다시가져와서 붙이는 작업 
            item = arr[head:N] + arr [0: rear%N]
        candid_set.add(item)
    
    decimal_arr =[]
    for w in candid_set:
        num_w = int(w,16)
        decimal_arr.append(num_w)
    
    decimal_arr.sort(reverse=True)
    
    ans = decimal_arr[K-1]
    print(f'#{tc}',ans)


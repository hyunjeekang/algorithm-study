#나무높이 

# import sys
# sys.stdin = open('input.text')

T = int(input())

for tc in range(1,T+1): #테스트 케이스 한개마다
    N = int(input()) #나무개수 
    arr = list(map(int,input().split()))
    arr.sort(reverse=True) # 나무 내림차순으로 정렬 

    MAX = max(arr) #최대값 선정
    q = []  # 최대값 기준 남은거
    for i in range(N):
        q.append((MAX-arr[i]))  #차이 보관
        q.sort(reverse=True) # 나머지도 내림차순으로 정렬 

    cnt = 0
    day = [1,2]
    while q: # 남은게 없어질때까지 해야하는 것.
            # for k in range(1,len(day)+1):
            for d in range(len(day)):
                    if day[d]: # 홀수번째날 
                        for j in range(N):
                            if q[j] %2 != 0 : #홀수면 
                                q[j] -= 1
                                cnt += 1
                            else:
                                q[j] -= 1
                                cnt += 1
                            
                    elif day[d]: #짝수번쨰날
                        for p in range(N):
                            if q[j] %2 == 0: #짝수면
                                q[j] -= 2
                                cnt += 1
                            else:
                                q[j] -=2
                                cnt += 1

    print(cnt )






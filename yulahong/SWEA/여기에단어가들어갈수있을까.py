T = int(input())

for tc in range(1, T+1):
   
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        count = 0
        for j in range(N):

            if arr[i][j] == 1:
                count += 1              

            if arr[i][j] == 0:
                if count == K:
                    ans += 1
                count = 0

        if count == K:
            ans += 1
     

    for j in range(N):
        count = 0
        for i in range(N):

            if arr[i][j] == 1:
                count += 1

            if arr[i][j] == 0:
                if count == K:
                    ans += 1
                count = 0
               
        if count == K:
            ans += 1
 

    print(f'#{tc} {ans}')


# N은 그리드 크기
# k는 단어 자리의 수
#
# 순회 행순회 모두 필요
# 흰색부분이 1 검은색 부분이 0
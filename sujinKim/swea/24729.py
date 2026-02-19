# import sys
# sys.stdin = open("input.txt")

T = int(input())  #각 테스트 케이스에 대해
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

 #그니까 이 문제는 각자 선수들의 실력차가 최대 k여야허고
 #선수를 최대로 모야아한다.
    #N명의 선수중에 한 사람을 기준으로 잡고 차이가 2 이하인 사람을
    #계속 +1씩 하면서 해야하나?
    arr.sort()  #정렬을 해버리면 맨 앞에가 가장 작은 수
    ans = 0 #최대 인원 초기화

    for n in range(N):  #n은 '가장 실력이 낮은 사람'의 인덱스
        cnt = 0
        for j in range(n, N): # n번째 사람부터 그 뒤 사람들을 검사
            #n번째 사람과 j번째 사람의 차이가 k이하인지?
            if arr[j] - arr[n] <= K: #나 자신도 팀의 일원이라 자기자신 빼기도 되나봄?
                cnt += 1
            else:  #arr를 정렬해놨으니까 k 넘어가면 더 볼 필요 없다.
                break

        if cnt > ans:
            ans = cnt

    print(f'#{tc} {ans}')





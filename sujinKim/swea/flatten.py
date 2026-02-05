#다른방법으로 풀어보고싶은 문제
#풀면서 카운트 방법&인덱스 개념이 헷갈림

T = 10  #총 10개의 테스트케이스 개수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for tc in range(1, T + 1):  #테스트케이스를 돌면서
    dump_num = int(input())  #덤프횟수를 입력받고
    arr = list(map(int, input().split()))  #각 상자의 높이값을 입력받음
    for dp in range(dump_num): #덤프를 할때마다 

        arr.sort() #정렬하고 
        arr[-1] -= 1 #맨 오른쪽꺼(젤 큰거)에서 하나 빠지고
        arr[0] += 1 #맨 왼쪽꺼(젤 작은거)에 하나 더해짐
    arr.sort() #다시 정렬


    print(f'#{tc} {arr[-1]-arr[0]}')




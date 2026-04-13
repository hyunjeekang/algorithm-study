
from collections import deque

N,K = map(int,input().split())

# 1. 우선 덱에 1부터 N 수를 담아
arr = deque()
for i in range(1,N+1):
    arr.append(i)
# print(arr)

result = deque()
# 2. K번째 수를 빼서 result에 담을거야.
# 근데 K번쨰를 뺄 때, K-1번째까지는 차례로 뒤에 옮겨

while arr:



    #3. 종료조건 result안이 전부 pop되면 result출력
    # if not arr:
    #     print("<"+",".join(map(str,result))+">")
    #     break
    # for j in range(1,N+1):
        #위 코드의 문제점 : N이 고정된 숫자. 하지만 arr에서 숫자를 하나씩 뺄 때마다 K번째를 찾는 행위는 매번 일어나야함
    for _ in range(K-1):
        # 즉, K-1번 뒤로 보내고, 1번 POP한다......
        # if j != K:
        #     arr.append(arr.popleft()) # K앞에 있던것들 빼서 원래 배열 뒤로 넣어야지
        #
        # elif j == K:
        #     result.append(arr.popleft())
        # * K-1번 동안 앞에꺼 뺴서 뒤로 넣기
        arr.append(arr.popleft())
    # for문이 끝나고 현재 arr의 맨 앞은 'K번째' 숫자. 이걸 result로 옮기기
    result.append(arr.popleft())

print("<"+", ".join(map(str,result))+">")










import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
T_line = input().strip()
if T_line:
    T=int(T_line)
else:
    exit()


#
# T = int(input())



# R = 뒤집기 D = 버리기
# R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수.
# 배열이 비어있는데 D를 사용한다? -> 에러발생

for i in range(1, T+1):
    p = input().strip()   #명령어
    n_line = input().strip() #arr의 개수
    if not n_line : continue
    n = int(n_line)
    arr = input().strip()

    content = arr[1:-1]  #대괄호 제거 후 덱에 넣음

    if n > 0:
        dq = deque(content.split(','))
    else:
        dq = deque()



    is_reversed = False
    is_error = False

    for j in p:
        if j == 'R':
            is_reversed = not is_reversed

        elif j == 'D':
            if not dq:

                is_error = True

                # print('error')
                break
            if is_reversed:
                dq.pop()    ###뒤집힌 상태이니까
            else:
                dq.popleft()

    if is_error:
        print('error')
    else:
        if is_reversed:
            dq.reverse()

        print("["+",".join(dq)+"]")






















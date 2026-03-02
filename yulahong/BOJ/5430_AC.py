# R: 배열에 있는 수의 순서를 뒤집는 함수(뒤집기)
# D: 첫번째 수를 버리는 함수(버리기), 배열이 비어있는데 D를 사용한 경우에는 에러 > popleft

# 인풋
# 첫쨰줄: 테케 수
# 각 테케 첫째줄: 수행할 함수 = p
# 둘쨰줄: 배열에 들어가 있는 수 = n
# 셋째줄: 배열

# 로직
# 인풋받은 배열을 이용해 새로운 덱 만들기
# R이 나올 경우 reverse메서드 사용
# D 나올 경우 popleft메서드 사용

import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    # 변수
    order = input().strip()
    n_str = input().strip()
    if not n_str: break # 예외 처리
    n = int(n_str)
    
    # 3. 배열 문자열 처리 
    raw_arr = input().strip()[1:-1]
    
    if n > 0:
        q = deque(raw_arr.split(','))
    else:
        q = deque()

    is_reversed = False
    error_occurred = False


    for cmd in order:
        if cmd == 'R':
            is_reversed = not is_reversed
        elif cmd == 'D':
            if not q:
                print("error")
                error_occurred = True
                break
            
            # 뒤집힌 상태면 오른쪽(pop), 아니면 왼쪽(popleft)
            if is_reversed:
                q.pop()
            else:
                q.popleft()


    if not error_occurred:
        if is_reversed:
            q.reverse()
        
        print("[" + ",".join(q) + "]")






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

from collections import deque

input()
order = input()
input()
order_list = list(map(int, input().split(',')))

q = deque(order_list)







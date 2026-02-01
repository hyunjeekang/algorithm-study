# 찾아본 것
# 1. 랜덤모듈
# 2. 한줄에 안 나올 때 input()> 어떻게 받을지 > 이건 좀 더 고민해볼걸 너무 이르게 찾아봄ㅜ

#기본 설계
# 1. 100이 넘지 않는 자연수 9개가 주어짐 >리스트로 표현
# 2. 그 중 7개의 합이 100이 되어야함
# 3. 조건문과 반복문 이용
# 4. 9개 중 랜덤한 숫자 7개 추출 > 순회 필요함 리스트 중 랜덤한 숫자 7개 추출한 식에 변수 할당
#     ㄱ. 조건1. 7개의 합이 100이 될 때 > 멈추고 7개의 값을 추출
#     ㄴ. 조건2. 7개의 합이 100이 아닐때 > 다시 올라가서 순회
# 5. 7개의 값 오름차순 정렬

import random

numbers = []
for _ in range(9): #> 9를 꼭 써야할까?
    num = int(input())
    numbers.append(num)

# 난쟁이 키 인풋 받는 식

for result in : # numbers 순회 처음에 작성 하지만 그러면 9번만 돌겠지? > 뭘 순회해야하는지 
    small = random.sample(numbers, 7)
    sum_numbers = sum(small)
    if sum_numbers != 100:
        continue
    elif sum_numbers == 100:
        print(small)
        # 다시 위로 돌아가서 반복하시오 continue?
        # 그럼 if 조건에 != 100을 쓴 다음 continue를 하고
        # elif로 == 100을 줘야할까?

    # if sum_numbers == 100:
    # print(small)
    # else:

a = sorted(result)  > #a는 리스트로 나온거 아닌가?
print (a) 

#런타임 에러남
#while문으로 다시 접근?




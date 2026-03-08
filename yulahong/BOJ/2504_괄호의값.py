# 4개의 기호: (), []
# 한쌍이어야만 함
# x가 올바른 괄호열이면 (x), [x] 도 올바른 괄호열
# x, y 모두 올바른 괄호열이면 결한한 xy도 올바른 괄호열임
# () = 2
# [] = 3
# (x) = 2*(x)
# [x] = 3*[x]
# xy = (xy) = (x) + (y)

# 변수
str_lst = list(input()) # ['(', '(', ')', '[', '[', ']', ']', ')', '(', '[', ']', ')']
# # 짝이 맞는지 검사 > if, count 사용

# 일단 짝이 맞는지 검사
# 짝이 안 맞으면 0 출력
# 짝이 맞으면 계산 시작 > 어떻게?

# if str_lst.count('(') != str_lst.count(')') or str_lst.count('[') != str_lst.count(']'):
#     ans = 0
# elif str_lst.count('(') == str_lst.count(')') and str_lst.count('[') == str_lst.count(']'):

# 여기서 괄호의 수가 같다고 올바른 괄호열이 아니란 것을 깨달음 ex. ([)]
# 길을 잃음...
# 그럼 수도 같고 대칭이어야 하나? 그것도 아님 [()[]] 대칭 아니지만 올바른 괄호열임 아어쩌란말이냐트위스트추면서...

# 생각해보니 스택 문제임 스택으로 접근하자...
stack = []

ans = 0
cal = 1
# 짝맞추기 스택 기본 원리
# for i in str_lst:
#     if i == '(' or i == '[':
#         stack.append(i)
#     elif i == ')'or i == ']':
#         stack.pop(i)
# 대칭검사까지 하고 어떻게 하는지 모르겠어서 제미나이한테 물어봄
for i in range(len(str_lst)):
    if str_lst[i] == '(':
        stack.append('(')
        cal *= 2
    elif str_lst[i] == '[':
        stack.append('[')
        cal *= 3
    elif str_lst[i] == ')':
        if not stack or stack[-1] != '(': #비어있거나 짝 안맞으면 답에 0을 저장하고
            ans = 0
            break #break
        if str_lst[i-1] == '(': #만약 짝이 맞으면
            ans += cal #답에 계산 결과를 누적하고
        stack.pop()
        cal //= 2 # 2를 나눠서 1로 원상복구
    elif str_lst[i] == ']':
        if not stack or stack[-1] != '[': 
            ans = 0
            break
        if str_lst[i-1] == '[':
            ans += cal
        stack.pop()
        cal //= 3

print(ans)


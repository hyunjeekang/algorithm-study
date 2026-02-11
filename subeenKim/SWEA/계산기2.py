def change_to_after(str): # 후위 표기식으로 바꾸는 함수
    after_expr = []
    stack = []
    priority = {'*':2, '+':1}

    for s in str :
        if '0' <= s <= '9':
            after_expr.append(s)
        else :
            while stack and priority[stack[-1]] >= priority[s]:
                after_expr.append(stack.pop())
            stack.append(s)
    while stack:
        after_expr.append(stack.pop())
    return after_expr

def calculate(alist): # 후위 표기식을 계산하는 함수
    stack = []
    A = change_to_after(alist)
    for a in A :
        if '0' <= a <= '9':
            stack.append(int(a))
        else :
            second = stack.pop()
            first = stack.pop()
            if a == '+':
                stack.append(first+second)
            else : # a == '*'
                stack.append(first*second)
    return stack[0]

for tc in range(1, 11):
    N = int(input())
    string = list(input())
    result = calculate(string)
    print(f'#{tc} {result}')
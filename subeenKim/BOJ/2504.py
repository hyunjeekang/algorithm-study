string = input()
stack = []

def check_digit(a):
    if type(a) == int :
        return True
    return False

is_right = True
for s in string :
    if s == '(' or s == '[': # 입력될 값이 여는 괄호
        stack.append(s)
    else : # 입력될 값이 닫는 괄호
        if not stack :
            is_right = False
            break
        # 스택 안에 무언가 있을 때
        if check_digit(stack[-1]):
            value = stack.pop()
            if stack and (stack[-1] == '(' or stack[-1] == '['):
                if s == ')' and stack[-1] == '(':
                    stack.pop()
                    if stack and check_digit(stack[-1]):
                        stack.append(stack.pop()+2*value)
                    else : # 안에 괄호가 있거나 스택이 비었음
                        stack.append(2*value)
                elif s == ']' and stack[-1] == '[':
                    stack.pop()
                    if stack and check_digit(stack[-1]):
                        stack.append(stack.pop()+3*value)
                    else : # 안에 괄호가 있거나 스택이 비었음
                        stack.append(3*value)
                else :
                    is_right = False
                    break
            else :
                is_right = False
                break
        elif stack[-1] == ']' or stack[-1] == ')':
            is_right = False
            break
        else : # 스택 젤 위에 있는 값이 여는 괄호
            if s == ')' and stack[-1] == '(':
                stack.pop()
                if stack and check_digit(stack[-1]):
                    stack.append(stack.pop()+2)
                else : # 안에 괄호가 있거나 스택이 비었음
                    stack.append(2)
            elif s == ']' and stack[-1] == '[':
                stack.pop()
                if stack and check_digit(stack[-1]):
                    stack.append(stack.pop()+3)
                else : # 안에 괄호가 있거나 스택이 비었음
                    stack.append(3)
            else :
                is_right = False
                break


if is_right and check_digit(stack[0]):
    print(stack[0])
else :
    print(0)
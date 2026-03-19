#백준 1406-에디터
import sys
input = sys.stdin.readline

#커서를 기준으로 좌우 스택 생성
left_stack = list(input().strip())
right_stack = []

m = int(input())

for _ in range(m):
    command = input().split()
    cmd = command[0]
   
    if cmd == 'L':
        #커서가 왼쪽으로 간다=왼쪽 스택에 있던 숫자가 오른쪽 스택으로 간다
        if len(left_stack)!=0 :
            right_stack.append(left_stack[-1])
            left_stack.pop()
    elif cmd == 'D':
        #커서가 오른쪽으로 간다=오른쪽 스택에 있던 숫자가 왼쪽 스택으로 간다
        if len(right_stack)!=0:
            left_stack.append(right_stack[-1])
            right_stack.pop()
    elif cmd == 'B':
        #숫자를 뺀다 = 팝
        if len(left_stack)!=0:
            left_stack.pop()
    elif cmd == 'P':
        #다음 숫자를 왼쪽 스택에 추가
        left_stack.append(command[1])

#문자열 조인해서 한번에 출력하기
print("".join(left_stack+right_stack[::-1]))
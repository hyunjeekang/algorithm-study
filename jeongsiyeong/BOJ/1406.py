import sys
input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []

m = int(input())

for _ in range(m):
    command = input().split()
    cmd = command[0]
   
    if cmd == 'L':
        if len(left_stack)!=0 :
            right_stack.append(left_stack[-1])
            left_stack.pop()
    elif cmd == 'D':
        if len(right_stack)!=0:
            left_stack.append(right_stack[-1])
            right_stack.pop()
    elif cmd == 'B':
        if len(left_stack)!=0:
            left_stack.pop()
    elif cmd == 'P':
        left_stack.append(command[1])

print("".join(left_stack+right_stack[::-1]))
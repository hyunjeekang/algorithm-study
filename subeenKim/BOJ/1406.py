import sys

input = sys.stdin.readline

string = input().strip()
N = int(input())
cursor = len(string) - 1

# right_stack은 순서가 반대!
left_stack, right_stack = list(string), []

for _ in range(N):
    command = input().split()
    if command[0] == 'P':
        left_stack.append(command[1])
    elif command[0] == 'L':
        if left_stack :
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()

print(''.join(left_stack + right_stack[::-1]))
import sys
input = sys.stdin.readline

N = int(input())
circle = []
for i in range(N):
    x, r = map(int, input().split())
    circle.append((x-r, i))
    circle.append((x+r, i))

circle.sort()

is_finish = False
for i in range(1, 2*N):
    if circle[i][0] == circle[i-1][0]:
        print('NO')
        is_finish = True
        break

if not is_finish:
    stack = []
    for i in range(2*N):
        x, num = circle[i]
        
        if not stack:
            stack.append(num)
        else:
            if stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)
                
    
    if not stack:
        print('YES')
    else:
        print('NO')
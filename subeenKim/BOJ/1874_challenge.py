n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []
answer = []
i = 0

for k in range(1, n+1):
    stack.append(k)
    answer.append('+')

    while stack and stack[-1] == nums[i]:
        stack.pop()
        answer.append('-')
        i += 1
        
if stack :
    print('NO')
else :
    for a in answer:
        print(a)  
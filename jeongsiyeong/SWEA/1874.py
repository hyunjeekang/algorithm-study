import sys

# 입력 속도를 높이기 위해 sys.stdin.readline 사용
n = int(sys.stdin.readline())

stack = []
result = []
count = 1
possible = True

for _ in range(n):
    target = int(sys.stdin.readline())

    # 1. 목표값(target)까지 스택에 1, 2, 3... 을 넣습니다 (PUSH)
    while count <= target:
        stack.append(count)
        result.append("+")
        count += 1

    # 2. 스택의 맨 위가 목표값과 같다면 꺼냅니다 (POP)
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        # 3. 스택의 맨 위가 목표값이 아니라면(더 크다면) 만들 수 없는 수열입니다
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")
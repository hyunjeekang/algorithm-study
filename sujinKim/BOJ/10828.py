N = int(input())
INPUT = []
for i in range(N):
    A = input().split()
    INPUT.append(A)

STACK = []
for j in INPUT:   # 입력받은 명령어들에서 하나씩 꺼내는데
    if j[0] == "push":   # 만약에 명령어가 push라면
        STACK.append(j[1])  # STACK에 인덱스1번째를 넣는다
    elif j[0] == "top": # 명령어가 "top"이라면
        if len(STACK) != 0:
            print(STACK[-1])
        else:
            print(-1)
    elif j[0] == "size": # 명령어가 "size"라면
        print(len(STACK))
    elif j[0] == "empty": # 명령어가 "empty"라면
        if len(STACK) != 0: # 스택의 사이즈가 0이 아니라면
            print(0)
        else:
            print(1)  # 비어있으면 1
    elif j[0] == "pop":
        if len(STACK) != 0:
            print(STACK.pop())  # 끝에 있는걸 빼서 출력
        else:
            print(-1)
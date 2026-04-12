import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

# LEFT = input() # 우선 커서 기준 전부 왼쪽이라 생각하고 입력 받아
LEFT = list(input().rstrip())
N = int(input()) # 입력할 명령어 개수
RIGHT = [] # 커서 옮겨지면 받을거
command = [] # 명령 받아놓은거
for i in range(N):
    C = input().split() # 명령어 받기

# print(command)

    if C[0] == "L": # 만약에 명령어가 L이라면, : 커서를 왼쪽으로 한 칸 옮김
    #그렇다면 왼쪽의 글자 한개가 오른쪽으로 옮겨지겠지
        if LEFT: # 만약에 LEFT 배열이 있다면
            RIGHT.append(LEFT.pop())
        else: # 커서가 맨 앞이라면
            pass # 무시됨
    elif C[0] == "D": # 만약에 명령어가 D라면, : 커서를 오른쪽으로 한 칸 옮김
        if RIGHT: # 만약에 RIGHT 배열이 있다면
            LEFT.append(RIGHT.pop(0)) # 오른쪽으로 움직이니까 오른쪽 첫번째가 왼쪽으로 가겟지?
        else:
            pass
    elif C[0] == "B": # 커서 왼쪽에 있는 문자를 삭제함
        if LEFT:
            LEFT.pop() # 왼쪽에 있는거 삭제
        else:
            pass
    else:
        # command[0] == "P": # 문자를 커서 왼쪽에 추가함

        LEFT.append(C[1])

# print(f"{LEFT}+{RIGHT}")
print(''.join(LEFT)+''.join(reversed(RIGHT)))

N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    elif line[0] == "pop": #명령어가 pop이라면 
        p = value.pop(0)
        print(p)
    elif line[0] == "size":
        print(len(value))
    elif line[0] == "empty":
        if len(value) == 0:
            print(1)
        else: 
            print(0)
    elif line[0] == "front":
        for i in range(len(value)):
            if value[i] == int(value[i]):
                print(value[i])
    else:  #명령어가 push가 아니라면 
        value.append(0)  #A에 0번째를 추가한다. (즉, 다른 명령어)






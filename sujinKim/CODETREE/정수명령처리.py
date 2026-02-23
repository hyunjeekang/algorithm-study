N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])  #입력받는 명령어들을 따로 리스트에 넣는다. 
   
    if line[0] == "push":
        value.append(int(line[1]))  #push를 하는 값을 value에 넣겠다. 
    elif line[0] == 'size': #명령어가 size라면 
        print(len(value)) #스택받은것들의 사이즈를 출력함. 
    elif line[0] == 'empty': #만약에 empty를 명령받았다면 
        if len(value) == 0 : #value(stack)이 없다면 
            print(1) #1을 출력 
        else: #있다면 
            print(0) #0을 출력 
    elif line[0] == 'top':  #만약 명령어가 top이라면 
        print(value[-1])  #쌓여져있던 스택의 맨 위에것을 출력한다. 
    elif line[0] == 'pop':
        p = value.pop() #맨 위에 있는 수를 뺴고
        print(p) #그 수를 출력 

   
    
# Please write your code here.
#push A : 정수A를 스택에 넣어 , 새로 들어온 정수는 상단부터 차례로 스택에 쌓임
#POP : 스택에서 가장 위에 있는 정수는 뺴고, 그 수를 출력한다. 
#SIZE 스택에 들어있는 정수의 개수를 출력
#EMPTY 비어있으면 1 아니면 0
#TOP 스택의 가장 위에 있는 정수를 출력한다. 
    
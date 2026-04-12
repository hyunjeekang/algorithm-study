import sys
data = sys.stdin.read().split() # 빠르게 입력을 받는다는건가? 

n = int(data[0])   #이렇게하면 data[0]=n이 된다는듯? 
stack= [] # 스택 넣는곳 
result = []  # '+','-' 결과값 받는 곳 
current = 1 # n이 8이잖아. 근데 현재 1부터 차례로 보면서 stack에 넣거나 빼서 result값에 +,-를 표시 
possible = True # 깃발선언 
for i in range(1,n+1):  #1부터 n까지
    num = int(data[i]) # num에 data의 i번째값을 정수화한 것을 num에 넣는다? 
    # if num == 
    while current <=num: # 현재값이 num(입력받았던값)보다 작거나 같다면 (== 다르니까)  
        stack.append(current) # 스택에 현재값을 넣고 
        result.append("+") # 결과값에 "+"를 넣는다 
        current += 1 # 그리고 다음 숫자 (현재값 다음값을 또 판별해야겠지?)

    if stack[-1] == num: # 만약 stack의 마지막값 (==제일 위에 값)이 num과 같다면 
        stack.pop() # stack의 가장 마지막값을 뺴고 
        result.append("-") # result에 "-"를 넣는다. 
    else: # stack의 마지막값이 같지 않다면 
        possible = False #깃발 선언 false로 하고 
        break # 빠져나온다. 
if possible: # 깃발선언이 true라면? 
    print("\n".join(result)) # 결과값을 띄어쓰기로 출력 
else:
    print("NO") # 불가능하다면 NO 

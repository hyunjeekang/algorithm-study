T = int(input())

for tc in range(1,T+1):
    a = input()

    STACK = [] # " ( " 전용칸 
    ans = True # STACK에서 꺼내는 괄호가 유효한 상태 
    for i in a: # 1. 괄호들을 a에서 하나씩 꺼낼게 
        if i == "(": # 만약에 꺼낸게 "(" 이거야 ! 그러면 
            STACK.append(i)
        elif i ==")": # 근데 만약에 " ) "라면 STACK에서 POP할건데
            ### 주의 ### pop할떄는 항상 pop할게 있는지 없는지 보자 
            if STACK:
                STACK.pop() # ") "의 짝인 " ( "을 찾아준다
            else: # 만약에 ")"이거 나오는 차례인데 STACK에 아무것도 없어 
                ans = False # 그러면 STACK에서 꺼낸 괄호들이 유효하지 않쥬?
                break
    if not ans or STACK :  # 꺼낸 괄호가 유효하지 않게 되거나 STACK에 뭐가 잇을때
        print("NO")
    else:
        print("YES")



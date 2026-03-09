# import sys
# # sys.stdin = open('input.txt','r')
# # #도전문제 
# arr = sys.stdin.readline().strip()

# stack = []  # 넣고 빼기만 하는 것. 
# plus = 0 # 더하기 ## plus += multi : 드디어 괄호가 닫혔네 ! 지금까지 쌓아온 배수를 결과값에 더하장
# ### 근데 바로 직전에 괄호가 열린 괄호일때만 더해야 중복 계산이 안됨 
# multi = 1 # 곱하기 : 내가 어떤 괄호들 안에 갇혀 있는지 

# for i in range(len(arr)):  # 입력받은 괄호를 앞에서부터 하나씩 보겠다.
#     if arr[i] == '(':  #열린중괄호라면 
#         stack.append('(') #열린중괄호를 우선 넣고 
#         multi *= 2 #2배해 <-----이게 젤 이해하기 힘듦
#     elif arr[i] == '[': #열린대괄호라면 
#         stack.append('[') #열린대괄호를 우선 넣고 
#         multi *= 3 #3배해 
#     elif arr[i] == ')': #닫힌중괄호라면 
#         if not stack or stack[-1] != '(':  #바로전에 넣은게 열린중괄호가 아니면 
#             plus = 0  #정상적인 괄호라면 열린게 없을리가  
#             break 

#         if arr[i-1] == '(': ### 직전에 열린중괄호였따면  
#             plus += multi

#         stack.pop()
#         multi //=2 # 이제 ( 를 벗어나서 앞으로 나올 값들은 2배를 해줄 필요가 없다 = 원복

#     elif arr[i] == ']':  #닫힌대괄호라면 
#         if not stack or stack[-1] != '[': # 바로전에 넣은게 열린대괄호가 아니면 
#             plus = 0 
#             break
#         if arr[i-1] == '[' ###직전에 열린대괄호였따면 
#             plus += multi 

#         stack.pop()
#         multi //=3 # 이제 [ 를 벗어나서 앞으로 나올 값들은 3배를 해줄 필요가 없다. 


# if stack:
#     print(0)
# else:
#     print(plus)





import sys

arr = sys.stdin.readline().strip() #한꺼번에 읽겟다 (?)

stack = []  # 괄호를 넣었다 뺼 공간 
plus = 0 # 찐 계산
multi = 1 #중첩된거 계산하는거 

for i in range(len(arr)):  
    if arr[i] == '(':  #열린중괄호라면 
        stack.append('(') # 스택에 넣고 
        multi *= 2 # 곱하기 2를 먼저 해준다. (중첩대비)

    elif arr[i] == '[': # 열린중괄호가 아니라 열린대괄호라면 
        stack.append('[') # 스택에 넣고
        multi *= 3 # 3배를 해준다 (중첩대비)

    elif arr[i] == ')': # 닫힌 중괄호라면 
        if not stack or stack[-1] != '(': # 스택에 아무것도 없거나 열린중괄호가 아니라면 
            plus = 0 # 찐 계산이 우선 0... 말이 안되는거지 
            break
        if arr[i-1] == '(': # 닫힌 중괄호에 + 그 전에께 열린중괄호라면 
            plus += multi # 계산했던거 plus에 넣는다 
        stack.pop() # 그리고 꺼내 
        multi //=2 #그리고 multi 곱했던거 원상복구 
    elif arr[i] == ']': # 닫힌대괄호가 나온다면 
        if not stack or stack[-1] != '[': # 스택이 비어있거나 전에께 열린 대괄호가 아니라면 
            plus = 0 # 말이 안되니까 결과값은 0이지 
            break
        if arr[i-1] == '[': # 닫힌 대괄호에 전에께 열린 대괄호라면 
            plus += multi # 계산했던거 찐계산에 넣고 
        stack.pop() # 꺼내 
        multi //= 3 # 그리고 곱했던거 원상복구 
if stack: 
    print(0) #스택에 뭐가 남아있으면 비정상 -> 0 
else:
    print(plus)



            




   


    








# import sys
# sys.stdin = open('input.txt','r')
# #도전문제 
arr = input()

stack = []  # 넣고 빼기만 하는 것. 
plus = 0 # 더하기 
multi = 1 # 곱하기 

for i in range(len(arr)):  # 입력받은 괄호를 앞에서부터 하나씩 보겠다.
    if arr[i] == '(':  #열린중괄호라면 
        stack.append('(') #열린중괄호를 우선 넣고 
        multi *= 2 #2배해 <-----이게 젤 이해하기 힘듦
    elif arr[i] == '[': #열린대괄호라면 
        stack.append('[') #열린대괄호를 우선 넣고 
        multi *= 3 #3배해 
    elif arr[i] == ')': #닫힌중괄호라면 
        if not stack or stack[-1] != '(':  #바로전에 넣은게 열린중괄호가 아니면 
            plus = 0  #정상적인 괄호라면 열린게 없을리가  
            break 

        if arr[i-1] == '(': ### 직전에 열린중괄호였따면  
            plus += multi

        stack.pop()
        multi //=2 #원래대로 ?

    elif arr[i] == ']':  #닫힌대괄호라면 
        if not stack or stack[-1] != '[': # 바로전에 넣은게 열린대괄호가 아니면 
            plus = 0 
            break
        if arr[i-1] == '[' ###직전에 열린대괄호였따면 
            plus += multi 

        stack.pop()
        multi //=3 #원래대로?
if stack:
    print(0)
else:
    print(plus)





            




   


    








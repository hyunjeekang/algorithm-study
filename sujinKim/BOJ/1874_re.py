# import sys
# sys.stdin = open("input.txt")
#
#
# n = int(input())
#
# q = [0]*n  # 이렇게 만들어야함.
# for i in range(n):
#     a = int(input())
#     q[i] = a
#
# # print(q)
#
# stack = [] # 담아두는곳
# result = [] # 출력할것 (+,-)
# for r in range(1,n+1):  # 1부터 8까지 돌면서 볼거야
#     for c in range(n): # 이거는 q의 순서를 볼거야.
#         if r != q[c]: # 1부터 8까지 볼건데 q의 첫번째랑 다르다면
#             stack.append(r) # 그 수를 스택에 넣어놔
#             result.append('+') # 그리고 결과값에 +를 넣어놔
#             break
# print(stack)
# print(result)

import sys
data = sys.stdin.read().split()

n = int(data[0])
stack = []  # 숫자를 담을 곳 
result = [] # 숫자를 넣고 뺴고할 연산값을 보관할곳 
current = 1 # 현재값 
possible = True #필요한 연산을 한 줄에 한 개씩 출력하는데 불가능한 경우도 있기 때문에.

for i in range(1,n+1): # 1부터 n까지 도는동안 
    num = int(data[i]) # 입력받았던 data값의 i번째 정수값을 num에 할당하겠다
    while current <= num: # 현재값이 num값보다 작으면 (현재값은 1,2,3,,순으로)
        stack.append(current) # stack에 현재값을 보관해둠 
        result.append("+") # 보관이니까 result값에 "+"를 넣음 . 
        current += 1 # 그리고 다음값을 넣을지 뺼지 생각해야하니까 +1 해서 현재값 갱신해주기 
        
    if stack[-1] == num: # stack의 마지막값이 num값과 같다면 
        stack.pop() # stack의 마지막값을 뺸다. 
        result.append("-") # 뺴줬으니까 결과값에 "-"를 넣어준다. 
    else: # 마지막값이 같지 않다면 (= stack의 마지막값이 num값과 같지 않다면) 
        possible = False # 불가능하다는 깃발 선언 
        break # 빠져나와줌 
if possible: # 가능하다면 결과값 쓰기 
    print("\n".join(result)) 
else:
    print("NO") # 불가능하다면 놉 말해줘 
    
    









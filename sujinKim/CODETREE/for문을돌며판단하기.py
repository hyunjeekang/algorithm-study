# N = int(input().split())

# for i in range(1,101-N):
#     N = N + i
    
#     if N >= 90:
#         print('A')
#     elif N >= 80:
#         print('B')
#     elif N >= 70:
#         print('C')
#     elif N >= 60:
#         print('D')
#     else:
#         print('F')

N = int(input())

for i in range(N,101):
    if i >= 90:
        print("A",end=" ")
    elif i >= 80:
        print("B",end=" ")
    elif i >= 70:
        print("C",end=" ")
    elif i >= 60:
        print("D",end=" ")
    else:
        print("F",end=" ")
        


#  1. input().split() + int() 같이 못 쓴다. 
#   - input().split() : 결과가 리스트
#   - int() 숫자 하나만 변환 가능
#  2. 점수를 루프마다 바꿔버림 입력한 점수 N을 계속 증가시키면서 등급을 출력 
#   - 즉, 점수 하나를 평가하는 코드가 아니라 점수를 계속 키우면서 등급이 바뀌는 과정을 찍는 코드 
#  3. for문을 써서 N=N+i로 하면 N이 계속 1씩 늘어날것이라 생각했는데 생각해보니까 i는 1,2,3,,,, 씩 늘어난다.

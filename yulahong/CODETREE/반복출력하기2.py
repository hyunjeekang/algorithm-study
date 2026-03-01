n = int(input())

def print_x(n): #함수 선언
    if n == 0: #0일 때
        return # 전의 값으로 리턴해

    print_x(n-1) #함수 내에서 함수 호출 4->3->2->1->0
    print('HelloWorld') #0에서 1을 불러와서 1에서 프린트 2불러와서 프린트 3불러와서 프린트 4불러와서 프린트

    #리턴 숨겨져 있음

print_x

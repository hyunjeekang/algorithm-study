import sys
##이거 진짜 몰라서 해설봄 


class Stack:  #스택 클래스 : Stack이란 건 이런 기능을 가지고 있다. 라고 정의한 도면  
    def start(self):  # 빈 스택 하나를 생성합니다.
        self.items = [] # 이 클래스로 만든 나의 보관함. 프로그램이 끝날 때까지 계속 유지해줘 
        #그리고 self.items는 push가 넣은 데이터를 pop하면 아까 보관함!하고 찾아갈 수 있는데
        #items=[]라고만 쓰면 이 함수 안에서 잠깐 쓰고 버릴 임시 메모지(지역변수)
        #items만 쓰면 push안의 items와 pop안의 items는 달라짐 
        

    def push(self, item):  # 스택에 데이터 넣기 : 괄호 열때 사용 
        self.items.append(item) 
        #self : 나 자신 : 이 기능이 속한 스택 객체 자기 자신임. 
        #item : 재료 : 스택에 새로 집어넣을 데이터를 담는 바구니 

    def empty(self):  # 스택이 비어있으면 True를 반환합니다.
        return not self.items
    
    # return no self.items와 같은 것
    # if len(self.items) == 0:
    #     return True
    # else:
    #     return False


    def size(self):  # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)

    def pop(self):  # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Stack is empty") #raise:에러를 강제로 발생시키기 

        return self.items.pop() #방금 열렸던 괄호 하나가 짝을 찾아서 나가기 위해 처리 

    def top(self):  # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty(): #
            raise Exception("Stack is empty")

        return self.items[-1]


# 변수 선언 및 입력:
string = input()  #괄호들을 입력받는다.
s = Stack() #Stack 클래스의 인스턴스를 생성한다. #실제물건 #이제 s는 만들었던 push,pop,empty 모두 가진 스택 바구니 

for char in string:
    if char == '(':
        s.push   # 즉, char가 )일떄 
        if s.empty(): #잘못된 괄호 짝을 찾아내는 결정적인 순간 
            print("No")
            sys.exit(0) #더 볼 것도 없이 당장 프로그램 끝내기 

        s.pop()

if s.empty():
    print("Yes")
else:
    print("No")

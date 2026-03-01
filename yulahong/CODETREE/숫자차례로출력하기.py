n = int(input())

# Please write your code here.
def print_list1(n): #오름차순 출력할 리스트
    if n == 0: #n이 0이 되면 리턴
        return

    print_list1(n-1) #함수 내부에서 함수 호출 0>1>2>3>4>5>6>7 이런식으로 불러옴
    print(n, end = " ") #오름차순 프린트됨

def print_list2(n): #내림차순 출력할 리스트
    if n == 0: #n이 0이 되면 리턴
        return

    print(n , end = " ") #내려 올때 바로 출력하면 7>6>5>4>3>2>1 내림차순 출력됨
    print_list2(n-1) # 함수 내부에서 함수 호출 다시 올라감

print_list1(n)
print() #줄 바꿈
print_list2(n)
n = int(input())

# Please write your code here.
def print_string(n):
    if n == 0:
        return

    print_string(n-1)
    print("HelloWorld")

print_string(n)



# def print_star(n): #1부터 n번째 줄까지 별을 출력하는 함수
#     print_star(n-1): #1부터 n-1번째 줄까지 출력하는 함수
#     print("*"*5)  #n번째 줄에 해당하는 별 출력 

# # print_star(n): 1번째 부터 n번째 줄까지 별을 알맞게 출력하는 함수라 정의한다면,
# # 이 함수는 print_star(n-1)를 먼저 수행하여 1번째부터 n-1번째 줄까지의 별을 알맞게 출력한 뒤, 
# # n번째 줄을 출력해보는 식으로 정의 

# def print_star(n):  # 1부터 n번째 줄까지 별을 출력하는 함수
#     if n == 0:      # n이 0이라면, 더 이상 진행하지 않고 
#         return      # 퇴각 

#     print_star(n-1)  #1부터 n-1번째 줄까지 출력하는 함수
#     print("*"*5)     # n번쨰 줄에 해당하는 별 출력 

# print("start")
# print_star(3)
# print("end")
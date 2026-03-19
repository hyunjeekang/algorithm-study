#백준 3273번 두 수의 합
#두 수의 합이 n인 수의 쌍 구하기
#투 포인터 문제

#숫자 개수
n = int(input())

#숫자들
number_list = list(map(int, input().split()))

#목표
goal = int(input())

number_list.sort()

low = 0
high = n-1
count = 0
while low < high:
    if number_list[low] + number_list[high] == goal:
        count+=1
        low+=1
        high-=1
    elif number_list[low] + number_list[high] < goal:
        low += 1
    else: 
        high -= 1

print(count)
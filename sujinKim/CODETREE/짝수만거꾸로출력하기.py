# N = int(input())
# arr = map(int,input().split())
# arr = arr.reversed()

# for i in arr:
#     if i % 2 == 0:
#         print(arr[i],end=' ')
    

# int(input()) : 정수 / 인덱스 x
# input()      : 문자열 / arr[0] = '1'
# input().split()  : 문자열 리스트 / arr[0] = '1'
# map(int, input().split()) : 숫자 리스트 / arr[0] = 1

N = int(input())
arr = list(map(int,input().split()))

for i in range(n-1,-1,-1):   #n-1(끝에서부터) -1(첫번째까지?) -1(거꾸로 한칸씩)
    if arr[i] % 2 == 0:
        print(arr[i],end=' ')

# # 새롭게 알게 된 사실 
# arr = [10,20,30,40]
# arr[-1] = 40
# arr[-2] = 30

# range(n-1,-1,-1) = range(start,stop,step)
# 여기서 stop의 -1은 : 멈추는 경계값  - > 이 숫자에 도달하기 직전까지 가라. -1직전까지 ! 글면 0까지겠쥬?



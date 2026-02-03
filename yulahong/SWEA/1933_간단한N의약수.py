# 반복문 순회는 range로
#     조건문으로 N 을 나눴을 때 나머지가 0이면 출력


N = int(input())

for i in range (1, N+1):
    if N % i == 0:
        print (i, end= ' ')

## 별 찍기 -2
# import sys
# sys.stdin = open('input.txt')


N = int(input())
for i in range(1,N+1): # 별 1개부터 ~ N개까지
    print(" "*(N-i),end="")
    print("*"*i)
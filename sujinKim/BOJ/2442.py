# import sys
# sys.stdin = open('input.txt')

N = int(input())
for i in range(N):
    print(" "*(N-i),end=" ")
    print("*"*(2*i+1))

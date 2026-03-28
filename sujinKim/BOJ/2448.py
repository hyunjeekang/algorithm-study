import sys
sys.stdin = open("input.txt")
### 규칙이 가장 작은단위(1-2-5)만들고 나면 아래(왼,오)에 2개 생기고
### 그렇게 또, new 작은단위가 생기면 그게 아래(왼,오)에 2개 생기고
### 그렇게 또, new 작은단위가 생기면 그게 아래(왼,오)에 생기는
# 이런식으로 재귀형식 같은데
result = [[0]*8 for in range(8)]

# 1. 가장 작은 단위를 만드는걸 재귀함수 써야할듯
def small_star(idx):
    global N
    n = 3
    N = N // n
    for idx in range(N):  # 가장 작은 단위를 8줄 쓰겠다.
        for i in range(n,0,-1):
            if i == n:
                print(" " * (i - 1) + "*")
            elif n > i > 1:
                print(" " + "*", end="")
                print(" " + "*")
            else:
                print("*" * (2 * n - 1))
    small_star(idx+1)



N = int(input())
# N = 3*2^k
# 3 6 12 24 48
# 가장 작은 단위가 N(24개) // 3 = 8 줄 있음
small_star(0)
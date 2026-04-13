# 백준 11931

import sys
sys.stdin = open("input.txt")
# N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램
# N개의 줄에는 숫자가 주어지는데 이 수는 절댓값이 1,000,000보다 작거나 같은 정수임.
# 수는 중복되지 않음

# 풀이 1
count_array = [0] * 10001
N = int(sys.stdin.readline())

# # N = int(input())
# arr = []
for _ in range(N):
    a = int(sys.stdin.readline())  # 입력받아지는 N개의 수
    count_array[a] += 1 # 입력받은 a의 갯수
#
# for i in range(10001): # i가 0부터 10000까지 1씩 커지며 반복
#     if count_array[i] != 0:
#         for _ in range(count_array[i]):
#             print(i)
for i in range(10000,-1,-1): # 즉, 내림차순을 하려면 뒤에서부터 훑게 만들면 됨
    if count_array[i] != 0:
        for _ in range(count_array[i]):
            print(i)
# 풀이 2 (일반적인 정렬 써서)
# N = int(input())
# arr = []
# for _ in range(N):
#     A = int(input())
#     arr.append(A)
#
# arr.sort(reverse=True)
#
# for i in arr:
#     print(i)

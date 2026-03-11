# 1부터 N까지 자연수 중에서 M개를 고른 수열 (중복 가능)
import sys
N, M = map(int, sys.stdin.readline().split())

def backtrack():
    if len(temp_list) == M:
        print(*temp_list)
        return
    
    for i in range(1, N+1):
        temp_list.append(i)
        backtrack()
        temp_list.pop()

temp_list = []
backtrack()
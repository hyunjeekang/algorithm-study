# N개의 자연수 중에서 M개를 고른 수열 (같은 수를 여러 번 골라도 된다.)

import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def backtrack():
    if len(temp_list) == M:
        print(*temp_list)
        return
    
    for i in range(N):
        temp_list.append(nums[i])
        backtrack()
        temp_list.pop()

temp_list = []
backtrack()
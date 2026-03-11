# N개의 자연수 중에서 M개를 고른 수열 (같은수 여러번 가능, 중복되는 수가 제시될 수 있음)

import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def backtrack():
    if len(temp_list) == M:
        order.append(temp_list[:])
        return
    
    prev = 0
    for i in range(N):
        if prev != nums[i]:
            temp_list.append(nums[i])
            prev = nums[i]
            backtrack()
            temp_list.pop()

temp_list = []
order = []
backtrack()
for o in order:
    print(*o)
# N개의 자연수 중에서 M개를 고른 수열 (고른 수열은 비내림차순이어야 함, 겹치는 숫자 제공될 수 있음)

import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def backtrack(start):
    if len(temp_list) == M:
        order_list.append(temp_list[:])
        return
    
    last_val = 0

    for i in range(start, N):
        if last_val != nums[i]:
            temp_list.append(nums[i])
            last_val = nums[i]
            backtrack(i+1)
            temp_list.pop()

order_list = []
temp_list = []
backtrack(0)
for o in order_list:
    print(*o)
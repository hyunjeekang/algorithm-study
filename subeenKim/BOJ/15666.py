# N개의 자연수 중에서 M개를 고른 수열 (중복 가능, 비내림차순, 같은 숫자 제시 가능)

import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def backtrack(start, temp):
    if len(temp) == M:
        order.append(temp[:])
        return
    
    prev = 0
    for i in range(start, N):
        if prev != nums[i]:
            temp.append(nums[i])
            prev = nums[i]
            backtrack(i, temp)
            temp.pop()

order = []
backtrack(0, [])
for o in order:
    print(*o)
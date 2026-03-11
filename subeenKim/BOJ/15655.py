# N개의 자연수 중에서 M개를 고른 수열 (고른 수열은 오름차순이어야 한다.)

import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def backtrack(start):
    if len(temp_list) == M:
        print(*temp_list)
        return

    for i in range(start, N):
        temp_list.append(nums[i])
        backtrack(i+1)
        temp_list.pop()

temp_list = []
backtrack(0)
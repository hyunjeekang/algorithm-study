# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기 (N개의 자연수 중에서 M개를 고른 수열)

import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

def backtrack():
    if len(temp_list) == M:
        print(*temp_list)
        return
    
    for i in range(N):
        if not visited[i]:
            temp_list.append(nums[i])
            visited[i] = True
            backtrack()
            temp_list.pop()
            visited[i] = False

temp_list = []
visited = [False]*N
backtrack()
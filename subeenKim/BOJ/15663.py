# N개의 자연수 중에서 M개를 고른 수열 (N개의 자연수 중 겹치는 수가 있음, 중복 안됨)

import sys; input=sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

def backtrack():
    if len(temp_list) == M:
        order_set.add(tuple(temp_list))
        return
    
    for i in range(N):
        if not visited[i]:
            temp_list.append(nums[i])
            visited[i] = True
            backtrack()
            temp_list.pop()
            visited[i] = False

order_set = set()
temp_list = []
visited = [False]*N
backtrack()
order_list = sorted(list(order_set))
for o in order_list:
    print(*o)
N, M = map(int, input().split())

nums = list(map(int, input().split()))
num_with_cnt = []
cur_num = nums[0]
cur_cnt = 1
for num in nums[1:]:
    if num != cur_num:
        num_with_cnt.append((cur_num, cur_cnt))
        cur_num = num
        cur_cnt = 1
    else:
        cur_cnt += 1
num_with_cnt.append((cur_num, cur_cnt))

def bin_search(m):
    left = 0
    right = len(num_with_cnt)-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if num_with_cnt[mid][0] == m:
            return num_with_cnt[mid][1]
        elif num_with_cnt[mid][0] < m:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for _ in range(M):
    m = int(input())
    print(bin_search(m))


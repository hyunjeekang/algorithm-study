T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().split())
    str = input()
    
    L = N // 4
    
    str_extend = str + str[:L-1]
    
    nums = set()
    for i in range(N):
        h_str = str_extend[i:i+L]
        nums.add(int(h_str, 16))
    sorted_nums = sorted(list(nums), reverse=True)
    print(f"#{test_case} {sorted_nums[K-1]}")
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.sort()
    
    cnt = 0
    for b in b_list:
        left = 0
        right = N-1
        
        prev_dir = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if a_list[mid] == b:
                cnt+=1
                break
            elif a_list[mid] < b:
                if prev_dir == 2:
                    break
                prev_dir = 2
                left = mid+1
            else:
                if prev_dir == 1:
                    break
                prev_dir = 1
                right = mid-1
    print(f'#{test_case} {cnt}')
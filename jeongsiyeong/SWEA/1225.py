from collections import deque

for test_case in range(1, 11):
    N = int(input()) 
    arr = list(map(int, input().split()))
    
    q = deque(arr)
    
    minus_val = 1
    
    while True:
        num = q.popleft()
        
        num -= minus_val
        
        if num <= 0:
            num = 0
            q.append(num)
            break
     
        q.append(num)
        
        minus_val = (minus_val + 1) % 5

    print(f'#{N}', end=" ")
    print(*q)
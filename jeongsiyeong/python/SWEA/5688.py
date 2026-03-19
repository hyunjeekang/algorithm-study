T = int(input())

""" for test_case in range(1, T+1):
    N = int(input())
    
    left = 1
    right = 1000000
    
    answer = -1
    while left <= right :
        mid = (left + right) // 2
        if mid**3 == N:
            answer = mid
            break
        elif mid**3 < N:
            left = mid+1
        else:
            right = mid-1
    
    print(f'#{test_case} {answer}') """

dict_n = {}    

for i in range(1, 1000001):
    dict_n.setdefault(i**3, i)
    
for test_case in range(1, T+1):
    N = int(input())
    answer = dict_n[N] if N in dict_n.keys() else -1
    print(f'#{test_case} {answer}')
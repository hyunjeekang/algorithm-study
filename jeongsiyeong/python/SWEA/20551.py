T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.reverse()
    cnt = 0
    
    for i in range(len(arr)-1):
        while arr[i] <= arr[i+1]:
            arr[i+1] -= 1
            cnt += 1
        if arr[i+1] <= 0:
            cnt = -1
            break
    
    print(f'#{test_case} {cnt}')
T = int(input())

arr = [0] * 31

arr[1] = 1
arr[2] = 3

for i in range(3, 31):
    arr[i] = arr[i-1] + 2*arr[i-2]

for test_case in range(1, T+1):
    N = int(input()) // 10
    print(f'#{test_case} {arr[N]}')
def partition(a_list, p, r):
    x = a_list[r]
    i = p - 1
    
    for j in range(p, r):
        if a_list[j] <= x:
            i+=1
            a_list[i], a_list[j] = a_list[j], a_list[i]
    
    a_list[i+1], a_list[r] = a_list[r], a_list[i+1]
    return i+1

def quickSort(a_list, l, r):
    if l<r:
        s = partition(a_list, l, r)
        quickSort(a_list, l, s-1)
        quickSort(a_list,s+1, r)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    quickSort(arr, 0, N-1)
    print(f'#{test_case} {arr[N//2]}')
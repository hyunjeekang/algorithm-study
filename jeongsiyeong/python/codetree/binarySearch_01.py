N, M = map(int, input().split())

arr = list(map(int, input().split()))

def bin_search(m):
    global N
    
    left = 0
    right = N-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == m:
            return mid+1
        elif arr[mid] < m :
            left = mid +  1
        else:
            right = mid - 1
    return -1

for _ in range(M):
    m = int(input())
    print(bin_search(m))
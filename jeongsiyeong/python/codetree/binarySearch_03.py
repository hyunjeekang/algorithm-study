N, M = map(int, input().split())

arr = list(map(int, input().split()))

querys = list(map(int, input().split()))

def bin_search(q):
    left = 0
    right = N - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == q:
            answer = mid+1
            right = mid - 1
        elif arr[mid] < q :
            left = mid + 1
        else:
            right = mid - 1
    return answer

for query in querys:
    print(bin_search(query))
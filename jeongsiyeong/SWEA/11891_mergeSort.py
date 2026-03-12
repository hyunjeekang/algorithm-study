def mergeSort(a_list):
    global cnt
    if len(a_list) <= 1:
        return a_list
    
    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    cnt += 1 if right[-1] < left[-1] else 0 
    return merge(left, right)

def merge(l, r):
    
    result = []
    l_c, r_c = 0, 0
    
    # Merge the two lists
    while l_c < len(l) and r_c < len(r):
        if l[l_c] <= r[r_c]:
            result.append(l[l_c])
            l_c += 1
        else:
            result.append(r[r_c])
            r_c += 1
            
    # Efficiently add any remaining elements
    if l_c < len(l):
        result.extend(l[l_c:])
    if r_c < len(r):
        result.extend(r[r_c:]) 
    return result

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = mergeSort(arr)
    
    print(f'#{test_case} {sorted_arr[N//2]} {cnt}')
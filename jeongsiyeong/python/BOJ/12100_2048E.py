N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def get_max(c_arr):
    tmp_mx = 0
    for a in c_arr:
        tmp_mx = max(tmp_mx, *a)
    return tmp_mx

def copy_arr(c_arr):
    tmp_arr = []
    for a in c_arr:
        tmp_arr.append(a[:])
    return tmp_arr

mx_block = get_max(arr)

def dfs(copied_arr, depth):
    global mx_block
    
    if get_max(copied_arr) * (2**(5-depth)) < mx_block:
        return
    
    if depth == 5:
        mx_block = max(mx_block, get_max(copied_arr))
        return
    
    # 오른쪽 밀기
    r_arr = copy_arr(copied_arr)
    for r in range(N):
        tmp_arr = []
        nums = [x for x in r_arr[r] if x != 0]
        
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx] == nums[idx-1]:
                tmp_arr.append(2 * nums[idx])
                idx -= 2
            else:
                tmp_arr.append(nums[idx])
                idx -= 1
        if idx == 0:
            tmp_arr.append(nums[0])
            
        for c in range(N-1, -1, -1):
            if tmp_arr:
                r_arr[r][c] = tmp_arr.pop(0)
            else:
                r_arr[r][c] = 0
    dfs(r_arr, depth+1)
    
    # 아래로 밀기:
    u_arr = copy_arr(copied_arr)
    for c in range(N):
        tmp_arr = []
        nums = [u_arr[r][c] for r in range(N) if u_arr[r][c] != 0]
        
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx] == nums[idx-1]:
                tmp_arr.append(2 * nums[idx])
                idx -= 2
            else:
                tmp_arr.append(nums[idx])
                idx -= 1
        if idx == 0:
            tmp_arr.append(nums[0])
            
        for r in range(N-1, -1, -1):
            if tmp_arr:
                u_arr[r][c] = tmp_arr.pop(0)
            else:
                u_arr[r][c] = 0
    dfs(u_arr, depth+1)
    
    # 왼쪽으로 밀기:
    l_arr = copy_arr(copied_arr)
    for r in range(N):
        tmp_arr = []
        nums = [x for x in l_arr[r] if x != 0]
        
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx+1]:
                tmp_arr.append(2 * nums[idx])
                idx += 2
            else:
                tmp_arr.append(nums[idx])
                idx += 1
        if idx == len(nums) - 1:
            tmp_arr.append(nums[idx])
            
        for c in range(N):
            if tmp_arr:
                l_arr[r][c] = tmp_arr.pop(0)
            else:
                l_arr[r][c] = 0
    dfs(l_arr, depth+1)
    
    # 위로 밀기
    d_arr = copy_arr(copied_arr)
    for c in range(N):
        tmp_arr = []
        nums = [d_arr[r][c] for r in range(N) if d_arr[r][c] != 0]
        
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx+1]:
                tmp_arr.append(2 * nums[idx])
                idx += 2
            else:
                tmp_arr.append(nums[idx])
                idx += 1
        if idx == len(nums) - 1:
            tmp_arr.append(nums[idx])
            
        for r in range(N):
            if tmp_arr:
                d_arr[r][c] = tmp_arr.pop(0)
            else:
                d_arr[r][c] = 0
    dfs(d_arr, depth+1)

dfs(arr, 0)
print(mx_block)
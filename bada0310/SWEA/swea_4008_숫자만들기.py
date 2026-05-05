# nums = 3 <= num <= 12
# operator 는 중복 순열 
# nums 사이에 대입 (nums 는 고정)
def calculate(res):
    total = nums[0]
    for i in range(len(res)):
        if res[i] == '+':
            total += nums[i+1]
        elif res[i] == '-':
            total -= nums[i+1]
        elif res[i] == '*':
            total *= nums[i+1]
        elif res[i] == '/':
            total = int(total/nums[i+1])
    return total
    
def rep_perm(depth):
    global max_val, min_val
    if depth == N-1:
        val = calculate(res)
        if val > max_val:
            max_val = val
        elif val < min_val:
            min_val = val 
        return
    for i in range(4):
        if visited_opr[i] > 0:
            visited_opr[i] -= 1
            res.append(operator[i])
            rep_perm(depth+1) # 재귀
            res.pop() # back tracking 
            visited_opr[i] += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operator = ['+', '-', '*', '/']
    visited_opr = list(map(int,input().split()))
    nums = list(map(int, input().split()))
    res = []
    max_val = -float('inf')
    min_val = float('inf')
    rep_perm(0)
    print(f'#{tc}',max_val - min_val)
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_val = -float('inf')
    min_val = float('inf')
    def rep_perm(depth,curr_val):
        global max_val, min_val
        
        if depth == N-1:
            max_val = max(max_val, curr_val)
            min_val = min(min_val, curr_val)
            return
        for i in range(4):
            if visited_opr[i] > 0:
                visited_opr[i] -= 1
                if  i == 0:
                    rep_perm(depth +1 , curr_val + nums[depth+1])
                elif i == 1:
                    rep_perm(depth+1, curr_val - nums[depth+1])
                elif i == 2:
                    rep_perm(depth+1, curr_val * nums[depth+1])
                elif i == 3: 
                    rep_perm(depth+1, int(curr_val / nums[depth+1]))
                visited_opr[i] += 1
    rep_perm(0, nums[0])
    print(f'#{tc}',max_val - min_val)
            
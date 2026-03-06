import sys
sys.stdin = open("algorithm-study\jeongsiyeong\SWEA\Sample_input (1).txt")
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    trees = list(map(int, input().split()))
    
    mx_tree = max(trees)
    odd = 0
    even = 0
    
    for h in trees:
        diff = mx_tree - h
        even += diff // 2
        odd += diff % 2
        
    while even > odd + 1:
        even -= 1
        odd += 2
    
    if odd > even:
        ans = odd * 2 -1
    elif odd < even:
        ans = even * 2
    else:
        ans = odd + even
    
    print(f'#{test_case} {ans}')
    
    
T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    results = [""] * N

    #90도
    for c in range(N):
        for r in range(N-1,-1,-1):
            results[c]+=arr[r][c]
        results[c]+=" "
    
    #180도 
    for r in range(N-1,-1,-1):
        for c in range(N-1,-1,-1):
            results[N-1-r] += arr[r][c]
        results[N-1-r]+=" "
    
    #270도
    for c in range(N-1,-1,-1):
        for r in range(N):
            results[N-1-c] += arr[r][c]
    
    for string in results:
        print(string)
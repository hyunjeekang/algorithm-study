T = int(input())
for tc in range(1,T+1):
    N,K =map(int,input().split())
    arr = input()
    arr2 = arr + arr 
    L = N // 4
    candid_set = set()
    for i in range(N):
        item = arr2[i:i+L]
        candid_set.add(item)
    
    res = []
    for w in candid_set:
        num_w = int(w,16)
        res.append(num_w)
    res.sort(reverse=True)
    ans = res[K-1]
    
    print(f'#{tc}',ans)
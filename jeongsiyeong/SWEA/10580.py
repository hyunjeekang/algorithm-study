T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    lines= []
    for _ in range(N):
        s, e = map(int, input().split())
        lines.append((s,e))
    lines.sort(key= lambda x: (x[0], -x[1]))
    
    
    cnt = 0
    for i in range(N):
        o_s, o_e = lines[i]
        for j in range(i, N):
            if o_s < lines[j][0] and o_e > lines[j][1]:
                cnt+=1
        
    print(f'#{test_case} {cnt}')
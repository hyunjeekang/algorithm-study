T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    pos = 0
    cur_v = 0
    
    for i in range(N):
        line = list(map(int,input().split()))
        
        if len(line) == 2:
            cmd = line[0]
            a = line[1]
            if cmd == 1 :
                cur_v += a
            elif cmd == 2:
                cur_v -= a
                if cur_v < 0:
                    cur_v = 0
        pos += cur_v
    
    print(f"#{test_case} {pos}")
        
        
    
COSTS = [k*k + (k-1)*(k-1) if k > 0 else 0 for k in range(50)]

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    houses = []
    for r in range(N):
        line = list(map(int, input().split()))
        for c in range(N):
            if line[c] == 1:
                houses.append((r, c))
    
    total_houses = len(houses) 
    max_total_profit = total_houses * M 
    
    max_houses = 0

    for r in range(N):
        for c in range(N):
            dist_count = [0] * (2 * N + 1)

            for hr, hc in houses:
                dist = abs(r - hr) + abs(c - hc)
                dist_count[dist] += 1
            
            covered_houses = 0
            for k in range(1, 2 * N + 2):
                covered_houses += dist_count[k-1]
                
                if COSTS[k] > max_total_profit:
                    break 
                
                if covered_houses <= max_houses:
                    continue
                
                if covered_houses * M >= COSTS[k]:
                    max_houses = covered_houses
                    
    print(f'#{test_case} {max_houses}')
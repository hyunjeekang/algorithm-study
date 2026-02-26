import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]

order = [0] * 9
order[3] = 0
mx_scores = 0

def simulate(order):
    scores = 0
    hitter_idx = 0
    
    for inning in range(N):
        out = 0
        base = 0 
        
        while out < 3:
            cur_hitter = order[hitter_idx]
            hit = hits[inning][cur_hitter]
            
            if hit == 0:
                out += 1
            else:
                base |= 1 
                
                base <<= hit
                
                scores += bin(base >> 4).count('1')
                
                base &= 14 
                
            hitter_idx = (hitter_idx + 1) % 9
            
    return scores

for p in permutations(range(1,9), 8):
    order = list(p[:3]) + [0] + list(p[3:])
    mx_scores = max(mx_scores, simulate(order))
print(mx_scores)
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]

mx_scores = 0

for p in permutations(range(1, 9), 8):
    order = p[:3] + (0,) + p[3:] 
    
    scores = 0
    hitter_idx = 0
    
    for inning in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0
        
        while out < 3:
            cur_hitter = order[hitter_idx]
            hit = hits[inning][cur_hitter]
            
            if hit == 0:
                out += 1
            elif hit == 1:
                scores += b3
                b1, b2, b3 = 1, b1, b2
            elif hit == 2:
                scores += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif hit == 3:
                scores += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif hit == 4:
                scores += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
                
            hitter_idx = (hitter_idx + 1) % 9
            
    if scores > mx_scores:
        mx_scores = scores

print(mx_scores)
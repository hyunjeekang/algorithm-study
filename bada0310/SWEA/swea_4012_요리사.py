def pair(team):
    score = 0
    for i in range(N//2):
        for j in range(N//2):
            score += grid[team[i]][team[j]]
    return score

def comb(start, depth):
    global min_val
    if min_val == 0:
        return
    if depth == N//2:
        team_a = res
        team_a_set = set(team_a)
        team_b = [i for i in range(N) if i not in team_a_set]
        diff = abs(pair(team_a) - pair(team_b))
        if diff < min_val:
            min_val = diff
        return
    for i in range(start,N):
        res.append(i)
        comb(i+1,depth+1)
        res.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid= [list(map(int,input().split())) for _ in range(N)]
    min_val = float('inf')
    res = [0]
    
    comb(1,1)
    print(f'#{tc}',min_val)
            
    
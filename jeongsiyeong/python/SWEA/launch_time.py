#점심 식사시간
def get_dist(sr, sc, pr, pc):
    return abs(pr-sr) + abs(pc - sc)

def get_stair_time(team_dists, stair_len):
    if not team_dists:
        return 0
    
    team_dists.sort()

    q = []

    for dist in team_dists:
        arrival_time = dist + 1

        if len(q) < 3:
            q.append(arrival_time + stair_len)
        else:
            prev_finish_time = q.pop(0)

            start_time = max(arrival_time, prev_finish_time)
            q.append(start_time + stair_len)
    return q[-1]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    persons = []
    stairs = []
    for r in range(N):
        line = list(map(int, input().split()))
        for c in range(N):
            if line[c] == 1:
                persons.append((r, c))
            elif line[c] > 1:
                stairs.append((r,c, line[c]))
    
    num_persons = len(persons)
    answer = float('inf')
    
    for mask in range(1 << num_persons):
        team1_dists = []
        team2_dists = []

        for i in range(num_persons):
            pr, pc = persons[i]

            if mask & (1 << i):
                sr, sc, slen = stairs[1]
                team2_dists.append(get_dist(sr,sc,pr,pc))
            else:
                sr, sc, slen = stairs[0]
                team1_dists.append(get_dist(sr,sc,pr,pc))
        time1 = get_stair_time(team1_dists, stairs[0][2])
        time2 = get_stair_time(team2_dists, stairs[1][2])

        current_case_time = max(time1, time2)

        answer = min(answer, current_case_time)
    print(f'#{test_case} {answer}')
    




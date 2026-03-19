C = int(input())

for test_case in range(C):
    players = [list(map(int, input().split())) for _ in range(11)]

    answer = 0
    visited = [False]*11

    def dfs(player_idx, current_score):
        global answer
        if player_idx == 11:
            answer = max(answer, current_score)
            return
        
        for i in range(11):
            if not visited[i] and players[player_idx][i]>0:
                visited[i] = True
                dfs(player_idx+1,current_score+players[player_idx][i])
                visited[i] = False

    dfs(0,0)
    print(answer)
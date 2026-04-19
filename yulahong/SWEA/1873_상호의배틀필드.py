# 이동(UDLR)
# 1. 현재 탱크의 위치 > tank_r, tank_c
# 2. 이동시킬 수 있는 곳인지 검사 > nr, nc
#    ㄱ. 이동 가능한 경우
#        > 탱크 이동 - nr, nc
#          + 고개도 돌리기 > 딕셔너리가 있으면 편하겠음
#    ㄴ. 이동 이동 불가능한 경우
#        > 탱크 이동 X
#          + 고개도 돌리기
  
# 포탄 발사(S)
# 1. 현재 탱크의 위치 / 방향 파악 > 얘도 딕셔너리로 해야겠다
# 2. 포탄 이동(아래 조건을 만족할 때까지, 둘 다 만족)
#    ㄱ. 맵 안쪽에 있을 때
#    ㄴ. 벽이 아닐 때
  
T = int(input())
  
# UDLR > 어떤 방향으로 옮길지(변화량), 어디로 고개 돌릴지 
order_dict = {
    'U': (-1, 0, '^'),
    'D': (1, 0, 'v'),
    'L': (0, -1, '<'),
    'R': (0, 1, '>'),
}
  
direction_dict = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}
  
def go(order):
    global tank_r, tank_c
  
    # 이동 > UDLR
    if order == 'U' or order == 'D' or order == 'L' or order == 'R':
        # ex) U > (-1, 0, '^')
        dr, dc, tank = order_dict[order]
  
        nr = tank_r + dr
        nc = tank_c + dc
        # 이동 불가능한 경우
        if nr < 0 or nr >= H or nc < 0 or nc >= W or graph[nr][nc] != '.':
            graph[tank_r][tank_c] = tank
            return
          
        # 이동 가능한 경우
        graph[tank_r][tank_c] = '.'
        graph[nr][nc] = tank
        tank_r, tank_c = nr, nc
  
    else:
        dr, dc = direction_dict[graph[tank_r][tank_c]]
  
        nr = tank_r + dr
        nc = tank_c + dc
  
        # 맵 안쪽일 때
        while 0 <= nr < H and 0 <= nc < W:
              
            # 벽을 만났음
            # ㄱ. 벽돌
            if graph[nr][nc] == '*':
                graph[nr][nc] = '.'
                break
  
            # ㄴ. 강철벽
            elif graph[nr][nc] == '#':
                break
              
            # 벽을 만나지 않았음
            nr += dr
            nc += dc
  
for tc in range(1, T+1):
    H, W = map(int, input().split())
  
    graph = [list(input()) for _ in range(H)]
  
    tank_r, tank_c = -1, -1
    for r in range(H):
        for c in range(W):
            if graph[r][c] == '<' or graph[r][c] == '>' or graph[r][c] == 'v' or graph[r][c] == '^':
                tank_r = r
                tank_c = c
                break
        if tank_r != -1:
            break
      
    input()
    orders = input()
  
    for order in orders:
        go(order)
  
    print(f'#{tc} ', end="")
    for r in range(H):
        print(''.join(graph[r]))
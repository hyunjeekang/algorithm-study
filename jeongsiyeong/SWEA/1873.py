T = int(input())

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    
    # 전차 상태 [r, c, direction]
    fortress = [0, 0, 0] 
    
    # 방향: 0:Right, 1:Down, 2:Left, 3:Up
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    # 전차 기호와 방향 매핑
    dir_dict = {'>': 0, 'v': 1, '<': 2, '^': 3} 

    
    # 1. 초기 전차 위치 찾기
    found = False
    for r in range(H):
        for c in range(W):
            if arr[r][c] in ['^', 'v', '<', '>']: 
                fortress[0], fortress[1] = r, c
                if arr[r][c] == '>': fortress[2] = 0
                elif arr[r][c] == 'v': fortress[2] = 1
                elif arr[r][c] == '<': fortress[2] = 2
                elif arr[r][c] == '^': fortress[2] = 3
                found = True
                break
        if found: break

    N = int(input())
    cmds = input()
    
    # 방향에 따른 전차 모양 리스트 (0, 1, 2, 3 순서)
    shape = ['>', 'v', '<', '^'] 

    def is_range(r, c):
        return 0 <= r < H and 0 <= c < W

    for cmd in cmds:
        if cmd == 'S':
            # 포탄 발사
            sr, sc = fortress[0], fortress[1]
            curr_dir = fortress[2]
            while True:
                sr += dr[curr_dir]
                sc += dc[curr_dir]
                if not is_range(sr, sc) or arr[sr][sc] == '#':
                    break
                if arr[sr][sc] == '*':
                    arr[sr][sc] = '.'
                    break
        else:
            new_dir = -1
            if cmd == 'U': new_dir = 3
            elif cmd == 'D': new_dir = 1
            elif cmd == 'L': new_dir = 2
            elif cmd == 'R': new_dir = 0
            
            if new_dir != -1:
                fortress[2] = new_dir # 1. 방향 전환
                # 현재 위치의 전차 모양을 일단 바뀐 방향으로 업데이트 (이동 못하더라도 방향은 바뀌니까)
                arr[fortress[0]][fortress[1]] = shape[new_dir] 
                
                nr = fortress[0] + dr[new_dir]
                nc = fortress[1] + dc[new_dir]
                
                if is_range(nr, nc) and arr[nr][nc] == '.':
                    arr[fortress[0]][fortress[1]] = '.' # 2. 옛날 위치 지우기
                    fortress[0], fortress[1] = nr, nc   # 3. 좌표 이동
                    arr[fortress[0]][fortress[1]] = shape[new_dir] # 4. 새로운 위치에 전차 모양 그리기

    print(f'#{test_case}', end=" ")
    for line in arr:
        print("".join(line))
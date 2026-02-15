from collections import deque

T = int(input())

for test_case in range(T):
    w, h = map(int, input().split())

    board = []
    f_q = deque()
    s_q = deque()

    visited = [[False]*w for _ in range(h)]

    for r in range(h):
        row = list(input()) 
        board.append(row)
        for c in range(w):
            if row[c] == '@':
                s_q.append((r,c))
                visited[r][c] = True
            elif row[c] == '*':
                f_q.append((r,c))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    time = 0
    is_exit = False
    
    while s_q:
        time += 1
        
        for _ in range(len(f_q)):
            fr, fc = f_q.popleft() 
            
            for i in range(4):
                nfr, nfc = fr + dr[i], fc + dc[i]
                
                if 0 <= nfr < h and 0 <= nfc < w:
                    if board[nfr][nfc] != '#' and board[nfr][nfc] != '*':
                        board[nfr][nfc] = '*'
                        f_q.append((nfr, nfc))

        for _ in range(len(s_q)):
            r, c = s_q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                
                if not(0 <= nr < h and 0 <= nc < w):
                    is_exit = True
                    break
                if board[nr][nc] != '#' and board[nr][nc] != '*' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    s_q.append((nr, nc))
            
            if is_exit:
                break
        
        if is_exit:
            break

    if is_exit:
        print(time)
    else:
        print("IMPOSSIBLE")
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for test_case in range(1, 11):
    N = int(input())
    
    arr=[]
    start_r, start_c = 0,0
    end_r, end_c = 0,0
    for r in range(16):
        line = input()
        row = []
        for c in range(16):
            if line[c] == '2':
                start_r = r
                start_c = c
            elif line[c] == '3':
                end_r = r
                end_c = c
            row.append(int(line[c]))
        arr.append(row)
    
    q = deque()
    q.append((start_r,start_c))
    ans=0
    visited = [[False]*16 for _ in range(16)]
    while q:
        cur_r, cur_c = q.popleft()

        if cur_r == end_r and cur_c == end_c:
            ans=1
            break
        for dir in range(4):
            nr = cur_r + dr[dir]
            nc = cur_c + dc[dir]

            if 0<=nr<16 and 0<=nc<16 and arr[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = True
    
    print(f'#{test_case}', ans)

    

    
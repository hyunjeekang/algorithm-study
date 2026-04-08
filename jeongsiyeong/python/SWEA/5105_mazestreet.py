from collections import deque

def solve():
    # Read number of test cases
    try:
        line = input().split()
        if not line: return
        T = int(line[0])
    except EOFError:
        return

    for test_case in range(1, T + 1):
        N = int(input())
        
        field = []
        sr = sc = gr = gc = 0
        
        for r in range(N):
            row_str = input()
            row_data = [int(char) for char in row_str]
            for c, val in enumerate(row_data):
                if val == 2:
                    sr, sc = r, c
                elif val == 3:
                    gr, gc = r, c
            field.append(row_data)
            
        queue = deque([(sr, sc, 0)])
        visited = [[False] * N for _ in range(N)]
        visited[sr][sc] = True
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        answer = 0
        
        while queue:
            cur_r, cur_c, cur_dist = queue.popleft()
    
            if cur_r == gr and cur_c == gc:
                answer = cur_dist - 1
                break
            
            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                
          
                if 0 <= nr < N and 0 <= nc < N:
                    if not visited[nr][nc] and field[nr][nc] != 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc, cur_dist + 1))
        
        print(f"#{test_case} {answer}")

if __name__ == "__main__":
    solve()
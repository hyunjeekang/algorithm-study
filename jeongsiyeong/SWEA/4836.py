T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 10x10 격자를 0으로 초기화
    grid = [[0] * 10 for _ in range(10)]
    
    for _ in range(N):
        # r: row(행, y축 개념), c: col(열, x축 개념)
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 범위 끝점(+1)까지 포함하여 색칠
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                grid[r][c] += color  # 1(빨강) 또는 2(파랑)를 누적해서 더함
                
    # 격자에서 값이 3(빨강+파랑)인 칸의 개수를 카운트
    result = 0
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 3:
                result += 1
                
    print(f"#{test_case} {result}")
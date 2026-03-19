import sys

sudoku = []
zeros = []
for r in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    sudoku.append(line)
    for c in range(9):
        if line[c] == 0:
            zeros.append((r, c))

def check_width(y):
    # (최적화) 전체를 셀 필요 없이, 방금 넣은 숫자가 중복되는지만 보면 됨
    target = sudoku[y]
    # 0을 제외한 숫자들 중에 중복이 있는지 확인
    # 리스트 컴프리헨션보다 단순 루프가 디버깅에 좋으므로 유지하되 로직 개선
    visited = [0] * 10
    for n in target:
        if n != 0:
            if visited[n]: return False
            visited[n] = 1
    return True

def check_height(x):
    visited = [0] * 10
    for i in range(9):
        n = sudoku[i][x]
        if n != 0:
            if visited[n]: return False
            visited[n] = 1
    return True

def check_area(y, x):
    # 2. 좌표 계산 수정: * 3을 해야 시작 인덱스가 됨 (0, 3, 6)
    top_y = (y // 3) * 3 
    top_x = (x // 3) * 3
    
    visited = [0] * 10
    for i in range(3):
        for j in range(3):
            n = sudoku[top_y+i][top_x+j]
            if n != 0:
                if visited[n]: return False
                visited[n] = 1
    return True

def dfs(index):
    if index == len(zeros):
        for r in range(9):
            print(*sudoku[r]) # 출력 방식 간소화
        sys.exit() # 정답 하나 찾으면 바로 종료
    
    r, c = zeros[index]
    
    for i in range(1, 10):
        sudoku[r][c] = i # 일단 놓아보고
        
        # 유망하면(Valid하면) 다음 단계로
        if check_width(r) and check_height(c) and check_area(r, c):
            dfs(index + 1)

    # 3. 복원 위치 수정: 
    # 1부터 9까지 다 넣어봤는데도 안 되면, 이 길은 틀린 길임.
    # 다시 0으로 비워두고 이전 단계(Back)로 돌아감.
    sudoku[r][c] = 0 

dfs(0)
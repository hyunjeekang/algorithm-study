# 원형큐 쓰는 문제
# 자석의 회전 정보는 회전시키려는 자석의 번호, 회전방향으로 구성되어 있다.
# 회전방향은 1 일 경우 시계방향이며, -1 일 경우 반시계방향이다.
# 날의 자성은 N 극이 0 으로, S 극이 1 로 주어진다.
# 크기 고정 가로로 8칸 세로 4칸 
# [1,2,4,8]
# 하나의 자석이 1 칸 회전될 때, 붙어 있는 자석은 
# 서로 붙어 있는 날의 자성과 다를 경우에만 인력에 의해 반대 방향으로 1 칸 회전된다.
# 2, 6만 자성을 확인 
# head tail 선언은 밖에서?
# arr = grid[row]

from collections import deque

def counterclock(row):# 반시계 방향 회전
    head[row] = (head[row]+1) % 8
    # tail[row] = (tail[row]+1) % 8

def clock(row):
    head[row] = (head[row]-1) % 8
    # tail[row] = (tail[row]-1) % 8

def get_target(arr,head):
    return arr[head]

def cnt(grid): # 점수 세는 함수 
    ans = 0
    for i in range(4): #[ 0, 1, 2, 3]
        if grid[i][head[i]] == 1:
            ans += 2**i
    return ans 

T = int(input())
for tc in range(1,T+1):
    K = int(input())
    grid = [list(map(int,input().split())) for _ in range(4)]
    head = [0,0,0,0]# head 위치를 담을 리스트 
    
    for _ in range(K):
        row_num, dir =map(int,input().split())
        idx = row_num -1
        
        dirs  = [ 0, 0, 0,0 ]# 회전 방향을 담을 것
        dirs[idx] = dir
        # dirs 표시하기 
        for i in range(idx, 0, -1): 
            rh = (head[i]+6) % 8
            lh = (head[i-1]+2) % 8
            
            if grid[i][rh] != grid[i-1][lh]:
                dirs[i-1] = -dirs[i]          
            else:                 
                break
        for i in range(idx,3):
            rh = (head[i]+2) % 8
            lh = (head[i+1]+6) % 8
            
            if grid[i][rh] != grid[i+1][lh]:
                dirs[i+1] = -dirs[i]
            else:
                break
            
        for i in range(4):
            if dirs[i] == 1:
                clock(i)
            elif dirs[i] == -1:
                counterclock(i)
        
    cost = cnt(grid)
    print(f'#{tc}',cost)




# def counterclock(row): 
#     arr = grid[row]
#     x = arr[0]
#     arr.pop(0)
#     arr.append(0)
#     return arr

# def clock(row): # 시계 방향 회전 
#     arr = grid[row] # 특정 행 
#     x = arr[-1]
#     arr.pop()
#     arr.insert(0, x)
#     return arr
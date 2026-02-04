n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

def is_range(x,y):
    return 0<=x<n and 0<=y<n

bishop_count = 0

#대각선 검사
#우상향 대각선 (/): 좌표 (r,c)에 대해 r+c값이 항상 같다
#좌상향 대각선 (\): 좌표 (r,c)에 대해 r-c값이 항상 같다.
black_pos = []
white_pos = []

black_diag1 = [False] * (2*n)
black_diag2 = [False] * (2*n)
white_diag1 = [False] * (2*n)
white_diag2 = [False] * (2*n)

max_count = 0

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            #체스판을 흑백으로 나누기-연산횟수 줄이기
            if (r+c)%2 == 0:
                black_pos.append((r,c))
            else:
                white_pos.append((r,c))


def dfs(index, count, pos_list,  diag1, diag2):
    global max_count

    #남은 칸수더해봤자 최대 개수보다 작거나 같으면 탐색 필요 없음-가지치기
    if max_count >= count + (len(pos_list) - index):
        return
    #탐색 성공
    if index == len(pos_list):
        max_count = max(max_count, count)
        return
    
    r,c = pos_list[index]

    dfs(index+1, count, pos_list,diag1,diag2)
    #백트래킹 
    if not diag1[r+c] and not diag2[r-c+n]:
        diag1[r+c] = True
        diag2[r-c+n] = True

        dfs(index+1, count+1, pos_list, diag1,diag2)
        #복원
        diag1[r+c] = False
        diag2[r-c+n] = False
        
#흑백 각각 탐색후 더하기
black_ans= -1
white_ans= -1

dfs(0,0,white_pos,white_diag1,white_diag2)
white_ans = max_count

max_count=0

dfs(0,0,black_pos,black_diag1,black_diag2)
black_ans = max_count

bishop_count = black_ans + white_ans
print(bishop_count)
#겹쳐진 횟수까지 세기 
#문제 ) n개의 직사각형이 주어질 때, 각 칸이 몇 번 칠해졌는지 누적해서 저장해라.
#출력 ) 1. 전체 칸 중 한 번 이상 칠해진 칸 수 2. 전체 칸 중 두 번 이상 칠해진 칸 수.

MAX_R =200
OFFSET = 100 #좌표음수대비
n = int(input())

rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
] #n줄을 읽어서 (x1,y1,x2,y2) 튜플로 저장 
#range(n) : 행이 아니라 입력 줄 개수 
# ex. (x1,y1,x2,y2) <- 1번 직사각형 정보
# ex. (x1,y1,x2,y2) <- 2번 직사각형 정보 

checked = [
    [0]*(MAX_R+1)
    for _ in range(MAX_R+1)
] #칠해졌는지 표시할 2차원 배열 만들기 
#여기서 range(MAX_R+1)은 진짜 2차원 배열의 행 개수 

 
#직사각형들을 하나씩 꺼내서 보드에 칠하기
for x1,y1,x2,y2 in rects:
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET


    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] +=1   #그 칸을 "칠했다"표시

#개수 초기화  
count1 = 0
count2 = 0

#전체 보드를 돌면서 1칸 칠해진 개수, 2칸 칠해진 개수 구하기 
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] >= 1:
            count1 += 1
        if checked[x][y] >= 2:
            count2 += 1 #칸 개수 세는 건데 왜 2를 더하냐. 겹친 칸 하나는 그냥 1칸임. 
            
print(count1)
print(count2)
#칠해진 영역의 둘레 길이 구하기 
#2차원 격자(정사각형 칸) 위에 직사각형들을 칠한다.
#칠해진 칸들의 겉둘레 길이를 구하라. 
#칠해진 칸 1개의 한 변 길이는 1이다. 
#상,하,좌,우 방향으로 인접한 두 칸이 모두 칠해져 있으면 , 그 사이의 변은 둘레가 아님
#격자 밖과 맞다항 있으면 그 변은 둘레로 센다. 
#좌표 범위

#-100 ≤ x1 < x2 ≤ 100

#-100 ≤ y1 < y2 ≤ 100

#입력
#첫 줄: 직사각형 개수 n
n = int(input())
MAX_R = 200
OFFSET = 100
#다음 n줄: x1 y1 x2 y2
#(직사각형은 (x1,y1)부터 (x2-1, y2-1)까지 칸을 칠함 → 즉 [x1, x2), [y1, y2))
rects = [
    tuple(map(int,input().split()))  #사각형 정보를 받는다
    for _ in range(n)  #n개의 사각형 정보를 받겠다. 

]

checked = [
    [0]*(MAX_R+1) #좌표의 빈칸(최대개수) 가로를 만든다. 
    for _ in range(MAX_R+1) #행의 개수(최대개수)를 늘린다.
]

for x1,y1,x2,y2 in rects:  #좌표가 음수일 수도 있으니까 양수로 만들어줌 
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] += 1 # 그 칸을 칠했다. 
length = 0
di = [1,-1,0,0]   #이웃칸을 찾는 버튼 
dj = [0,0,1,-1]
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] >= 1: # 칠해진 칸이라면(1번 이상)
            for k in range(4):  #이 칸의 4개의 방향을 하나씩 검사한다. 
                nx =  x + di[k]  #현재 칸 옆에 붙어있는 이웃칸 좌표 
                ny = y + dj[k]
                #이 면의 바깥쪽은 공기인가? 
                if nx < 0 or nx > MAX_R or ny < 0 or ny > MAX_R:
                    #보드 밖이라면? 즉, 이 면 바깥에는 아예 칸이 없고 공기.. 즉 둘레 구하기 
                    length += 1
                elif checked[nx][ny] == 0:
                    #보드 안인데 색칠 안된 칸
                    #이 면 바깥 칸이 0 -> 색칠 안됨->공기 ->둘레 
                    length += 1
                   

print(length)



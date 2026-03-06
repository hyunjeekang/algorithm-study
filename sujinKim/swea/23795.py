#우주 괴물
import sys
sys.stdin = open('input.txt')

T = int(input())
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Sr = Sc = 0 #이걸 표시 왜하지? 강사님은 하시던디 
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                Sr,Sc = r,c  #괴물의 위치 지정

    for i in range(4): #4방향을 볼게
        #근데 nr,nc가 벽을 만날때까지 탐색하는거잖아
        #그래서 그 레이저를 1로 표시할게 ㅇㅇ
        for j in range(1,N-1): #이동을 1칸부터 최대 N-1칸까지 가능
            nr = Sr + dr[i]*j
            nc = Sc + dc[i]*j

            if 0<=nr<N and 0<=nc<N : #경계 췍
                if arr[nr][nc] == 1: #주변애들이 1이라면
                    break #멈춤?
                else:
                    arr[nr][nc] = 1 #1이 아니라면 1을 대입하기 ?
            else: # 경계값 밖이라면
                break #빠져나옴 ???
    cnt = 0
    #레이저 부분 1표시하고 나서 전체 싹 돌면서 0만 찾기 
    for f in range(N):
        for d in range(N):
            if arr[f][d] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')


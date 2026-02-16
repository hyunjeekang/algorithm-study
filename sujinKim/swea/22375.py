import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #케이스 별로 스위치 개수
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    ans = 0 #스위치 누른횟수
    for n in range(N):
        if Ai[n] != Bi[n]:#뭔가 각 행끼리 보면서 서로 다른 시점의 열부터 스위치를 눌러야할듯?
            ans += 1 #다를떄마다 스위치 누른다.
            #밑에 있는 for문은 버튼 한 번으로 인해 뒤에 있는 전등들이 줄줄이 바뀌는 현상
            #
            for j in range(n,N): #다른 지점인 n부터 끝까지인 N까지 하나씩 꺼낼 때
                if Ai[j] == 0:  #Ai의 j번째가 0이라면
                    Ai[j] = 1   #Ai의 j번째를 1로 바꿔주고
                else:          #Ai의 j번째가 0이 아니라면 즉 1이라면
                    Ai[j] = 0  #Ai의 j번쨰를 0으로 바꿔줌
    print(f'#{tc} {ans}')

            #여기서부터 이제 Ai가 Bi랑 같아질때까지 바꿔줘야함.









#N개의 전등이 설치
#전등이 켜진 상태 =1
#전등이 꺼진 상태 =0

#초기상태 000
#2번 스위치 011
#3번 스위치 010


#이 문제의 핵심 : i번째 스위치를 누르면 i번쨰부터 N번째까지 모든 전등의 상태가 바뀐다.
#단순히 몇 번을 눌러야 하는가에 집중하면 됨.


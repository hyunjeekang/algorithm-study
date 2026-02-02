chess = [list(input()) for _ in range(8)]
cnt = 0

for i in range(8) :
    if i % 2 == 0 : # 홀수 번째 줄 : 하얀 칸으로 시작
        pass
        for j in range(8) :
            if j % 2 == 0 :
                if chess[i][j] == 'F' :
                    cnt += 1
    else : # 짝수 번째 줄 : 검정 칸으로 시작
        for j in range(8) :
            if j % 2 == 1 :
                if chess[i][j] == 'F' :
                    cnt += 1
print(cnt)
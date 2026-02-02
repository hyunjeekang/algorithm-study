import math

loc_list = list(map(int, input().split()))
aX, aY = loc_list[0:2]
bX, bY = loc_list[2:4]
cX, cY = loc_list[4:]

# 한 직선 위에 있으면 평행사변형 안만들어짐
if (aX == bX) and (aX == cX) : # x축과 평행
    print(-1.0)
elif (aY == bY) and (aY == cY) : # y축과 평행
    print(-1.0)
else :
    if (bX == aX and cX != aX) or (bX != aX and cX == aX) :
        line_ab = math.sqrt((aX - bX)**2 + (aY - bY)**2)
        line_bc = math.sqrt((bX - cX)**2 + (bY - cY)**2)
        line_ca = math.sqrt((cX - aX)**2 + (cY - aY)**2)

        line_len = [line_ab, line_bc, line_ca]
        line_len.sort()
        answer = 2 * ((line_len[2] + line_len[1]) - (line_len[1] + line_len[0]))
        print(answer)
    
    elif (bY - aY)/(bX - aX) == (cY - aY)/(cX - aX) :
        print(-1.0)
    
    else :
        line_ab = math.sqrt((aX - bX)**2 + (aY - bY)**2)
        line_bc = math.sqrt((bX - cX)**2 + (bY - cY)**2)
        line_ca = math.sqrt((cX - aX)**2 + (cY - aY)**2)

        line_len = [line_ab, line_bc, line_ca]
        line_len.sort()
        answer = 2 * ((line_len[2] + line_len[1]) - (line_len[1] + line_len[0]))
        print(answer)
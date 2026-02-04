King, Stone, N = map(str, input().split())
N = int(N)
move = [input() for _ in range(N)]

def moving(M, x, y) :
    # 'R 또는 L'과 'B 또는 T'는 함께 나올 수 있음
    # R 또는 L 둘 중에 하나만 나올 수 있음
    if 'R' in M:
        x = chr(ord(x) + 1)
    elif 'L' in M:
        x = chr(ord(x) - 1)

    # B 또는 T 둘 중에 하나만 나올 수 있음
    if 'B' in M:
        y = str(int(y) - 1)
    elif 'T' in M:
        y = str(int(y) + 1)
    return x, y

for m in move :
    King_x, King_y = moving(m, King[0], King[1])
    # 킹 위치가 정상적인지 확인
    if ('A' <= King_x <= 'H') and (1 <= int(King_y) <= 8):
        # 킹이 움직인 위치가 돌의 위치라면
        if King_x + King_y == Stone :
            # 돌의 움직이려는 위치가 정상적인지 확인
            Stone_x, Stone_y = moving(m, Stone[0], Stone[1])
            if ('A' <= Stone_x <= 'H') and (1 <= int(Stone_y) <= 8) :
                King = King_x + King_y
                Stone = Stone_x + Stone_y
        else :
            # 킹의 위치만 업데이트
            King = King_x + King_y

print(King)
print(Stone)
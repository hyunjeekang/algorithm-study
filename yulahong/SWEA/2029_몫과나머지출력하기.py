# # #첫 줄에는 T 변수 할당하기
# a, b 변수 할당하기
# 반복문 사용하기 >몫과 나머지를 t번만큼 나와야하기 때문에
# # 표기 방식은 몫 나머지

T = int(input())

for tc in range(1,T+1):
    a, b = map(int, input().split())
    c = a // b
    d = a % b
    print(f'#{tc} {c} {d}')


    #오답노트
    # a,b 데이터를 받는 위치가  반복문 밖이라서 딱 한번 가져옴!!
# 남은 남 여는 여끼리
# 같은 학년끼리
# 첫번째 정수 N = 참가 학생 수
# K = 한 방에 배정할 수 있는 최대 인원 수
# 성별 S, 학년 G = 0(여), 1(남)

N, K = map(int, input().split())
# S, G = map(int, input().split())

girl_1 = 0
girl_2 = 0
girl_3 = 0
girl_4 = 0
girl_5 = 0
girl_6 = 0

boy_1 = 0
boy_2 = 0
boy_3 = 0
boy_4 = 0
boy_5 = 0
boy_6 = 0

for _ in range(N):
    S, G = map(int, input().split()) #인풋받음

    if S == 0 and G == 1:
        girl_1 += 1
    if S == 0 and G == 2:
        girl_2 += 1
    if S == 0 and G == 3:
        girl_3 += 1
    if S == 0 and G == 4:
        girl_4 += 1
    if S == 0 and G == 5:
        girl_5 += 1
    if S == 0 and G == 6:
        girl_6 += 1


    if S == 1 and G == 1:
        boy_1 += 1
    if S == 1 and G == 2:
        boy_2 += 1
    if S == 1 and G == 3:
        boy_3 += 1
    if S == 1 and G == 4:
        boy_4 += 1
    if S == 1 and G == 5:
        boy_5 += 1
    if S == 1 and G == 6:
        boy_6 += 1

result = [
girl_1,
girl_2,
girl_3,
girl_4,
girl_5,
girl_6,
boy_1,
boy_2,
boy_3,
boy_4,
boy_5,
boy_6,]

ans = 0

for i in result:
    ans += i // K
    if i % K > 0:
        ans += 1

print(ans)




